import json
from typing import TYPE_CHECKING

from llpy import WSClient, logger

if TYPE_CHECKING:
    from handler import Handler


class WebSocket:
    def __init__(self, ws_address: str, token: str, handler: "Handler"):
        self.ws = WSClient()
        self.ws_address = ws_address
        self.token = token
        self.handler = handler
        self._connecting = False

        if not self.ws_address.endswith("/"):
            self.ws_address += "/"

        self.ws.listen("onLostConnection", self.on_lost_connection)

    def on_connect(self, is_connected: bool):
        self.ws.send(json.dumps({"token": self.token}))
        if is_connected:
            logger.info(f"WebSocket connected to {self.ws_address}")

    def on_lost_connection(self, status: int):
        self.ws.close()
        self._connecting = False
        logger.warn(f"WebSocket lost connection, status code: {status}")

    def reconnect(self, _=None):
        if self.ws.status == self.ws.Closed and self._connecting is False:
            self._connecting = True
            self.ws.connectAsync(self.ws_address, self.on_connect)

    def send(self, msg: str):
        if self.ws.status != self.ws.Open:
            logger.warn("WebSocket is not connected, failed to send message!")
            return None
        self.ws.send(msg)

    def heartbeat(self):
        self.send(json.dumps({"event_name": "Heartbeat"}))

    def forward(self, data: dict):
        msg = self.handler.handle(data)
        self.send(json.dumps(msg))
