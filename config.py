import yaml
from pathlib import Path
from typing import TypedDict, List, Optional

from llpy import logger


class Config(TypedDict):
    WebSocketAddress: str
    HttpHost: str
    HttpPost: int
    Token: str
    ReconnectInterval: int
    Timeout: int
    ForwardEvents: List[str]


plugin_dir = Path(__file__).parent


default_config = """
WebSocketAddress: ws://127.0.0.1:8080/llbds\n
# NoneBot2 的 WebSocket 地址, 由 .env 文件中的 HOST 和 PORT 决定\n\n
HttpHost: 127.0.0.1\n
# LLBDS 的 HTTP API 地址\n\n
HttpPost: 8081\n
# LLBDS 的 HTTP API 端口\n\n
Token: your_token\n
# 鉴权 Token, 由 .env 文件中的 LLBDS_TOKEN 决定\n\n
ReconnectInterval: 5\n
# WebSocket 重连间隔, 单位为秒, 默认为 5 秒\n\n
Timeout: 60\n
# 缓存对象的超时时间, 单位为秒, 默认为 60 秒\n\n
ForwardEvents:\n
  # 需要转发的事件列表, 参阅 https://docs.litebds.com/zh-Hans/#/LLSEPluginDevelopment/EventAPI/Listen 及相关内容\n
  - PreJoin\n
  - Join\n
  - Left\n
  - Respawn\n
  - PlayerDie\n
  - Chat\n
  - ChangeDim\n\n
"""


def load_config() -> Optional[Config]:
    try:
        with open(plugin_dir / "config.yml", "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        with open(plugin_dir / "config.yml", "w", encoding="utf-8") as f:
            f.write(default_config)
        logger.warn(f"{plugin_dir / 'config.yml'} 不存在, 已创建默认配置文件，请编辑后重试")
        return Config(
            WebSocketAddress="ws://127.0.0.1:8080/llbds",
            HttpHost="127.0.0.1",
            HttpPost=8081,
            Token="your_token",
            Timeout=60,
            ForwardEvents=[
                "PreJoin",
                "Join",
                "Left",
                "Respawn",
                "PlayerDie",
                "Chat",
                "ChangeDim",
            ],
        )
