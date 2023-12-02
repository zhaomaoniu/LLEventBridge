import json
from enum import IntEnum
from typing import TYPE_CHECKING

from llpy import WSClient, logger

if TYPE_CHECKING:
    from handler import Handler


class WebSocketStatus(IntEnum):
    Connecting = 0
    Connected = 1
    Disconnected = 2


class WebSocket:
    def __init__(self, ws_address: str, token: str, handler: "Handler"):
        self.ws = WSClient()
        self.ws_address = ws_address
        self.token = token
        self.handler = handler
        self.status = WebSocketStatus.Disconnected

        if not self.ws_address.endswith("/"):
            self.ws_address += "/"

        self.ws.connectAsync(ws_address, self.on_connect)
        self.ws.listen("onLostConnection", self.on_lost_connection)

    def on_connect(self, is_connected: bool):
        self.status = WebSocketStatus.Connecting

        if is_connected:
            self.status = WebSocketStatus.Connected
            self.ws.send(json.dumps({"token": self.token}))
            logger.info(f"WebSocket connected to {self.ws_address}")
        else:
            self.status = WebSocketStatus.Disconnected
            logger.warn(
                f"WebSocket failed to connect to {self.ws_address}, retrying..."
            )
            self.reconnect()

    def on_lost_connection(self, status: int):
        self.status = WebSocketStatus.Disconnected
        logger.warn(f"WebSocket lost connection, status code: {status}")
        self.reconnect()

    def reconnect(self, _ = None):
        if self.status != WebSocketStatus.Disconnected:
            return None
        self.ws.connectAsync(self.ws_address, self.on_connect)

    def send(self, msg: str):
        if self.status != WebSocketStatus.Connected:
            logger.warn("WebSocket is not connected, failed to send message!")
            return None
        self.ws.send(msg)

    def forward(self, data: dict):
        msg = self.handler.handle(data)
        self.send(json.dumps(msg))
