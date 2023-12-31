<div align="center">

# LLEventBridge

_✨ LLBDS 转发事件 & 开放API 插件 ✨_

</div>

## 概览
LLEventBridge 是用于对接 nonebot-adapter-llbds 的 LLBDS Python 插件，目前正在锐意开发中（）

## 使用
将仓库克隆到本地，把仓库文件夹下的所有文件打包为 `LLEventBridge.zip`，再重命名为 `LLEventBridge.llplugin`

将 `LLEventBridge.llplugin` 移动到 LLBDS / plugins 文件夹中，运行 LLBDS

等待 LLBDS 开始正常运行后关闭 LLBDS，进入 LLBDS / plugins / python / EventBridge 文件夹中，修改 config.yml

### 配置
```
WebSocketAddress: ws://127.0.0.1:8080/llbds
# NoneBot2 的 WebSocket 地址, 由 NoneBot2 机器人目录下 .env 文件中的 HOST 和 PORT 决定

HttpHost: 127.0.0.1
# LLBDS 的 HTTP API 地址

HttpPost: 8081
# LLBDS 的 HTTP API 端口

Token: your_token
# 鉴权 Token, 由 NoneBot2 机器人目录下 .env 文件中的 LLBDS_TOKEN 决定

ReconnectInterval: 5
# WebSocket 重连间隔, 单位为秒, 默认为 5 秒

HeartbeatInterval: 5
# 心跳间隔, 单位为秒, 默认为 5 秒

Timeout: 60
# 缓存对象的超时时间, 单位为秒, 默认为 60 秒

ForwardEvents:
  # 需要转发的事件列表, 参阅 https://docs.litebds.com/zh-Hans/#/LLSEPluginDevelopment/EventAPI/Listen 及相关内容
  - PreJoin
  - Join
  - Left
  - Respawn
  - PlayerDie
  - Chat
  - ChangeDim

```

重新打开 LLBDS 即可

当你看到类似 `WebSocket connected to ws://127.0.0.1:8080/llbds` 的日志时，表明 EventBridge 开始正常运行

## 反馈
可以直接提 issues 或者 pull requests

不会用的话可以来群里(666808414)@Staff Z，一般周末和工作日晚上在线

## 感谢
[lgc2333](https://github.com/lgc2333): 项目起因   
[WindowsSov8](https://github.com/WindowsSov8forUs): 帮助解决了 nonebot-adapter-llbds 与 EventBridge 连接问题