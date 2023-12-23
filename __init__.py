from llpy import HttpServer, logger, setInterval, mc, ll

from config import load_config
from event import EventForwarder
from handler import Handler
from websocket import WebSocket
from api import APIHandler


ll.registerPlugin("EventBridge", "转发事件 & 开放API", [0, 0, 1])


logger.info("EventBridge is initializing...")

config = load_config()
handler = Handler(config["Timeout"])
websocket = WebSocket(config["WebSocketAddress"], config["Token"], handler)
http_server = HttpServer()
event_forwarder = EventForwarder(websocket, config["ForwardEvents"])
http_server.listen(config["HttpHost"], config["HttpPost"])
api_handler = APIHandler(http_server, mc, config["Token"], handler)

setInterval(websocket.reconnect, config["ReconnectInterval"] * 1000)
setInterval(websocket.heartbeat, config["HeartbeatInterval"] * 1000)

# 监听事件
for event in config["ForwardEvents"]:
    # 将大驼峰处理为下划线
    event_name = "".join(["_" + i.lower() if i.isupper() else i for i in event]).lstrip("_")
    if hasattr(event_forwarder, f"on_{event_name}"):
        logger.info(f"Listening event {event}...")
        mc.listen(f"on{event}", getattr(event_forwarder, f"on_{event_name}"))
