import json
from typing import TYPE_CHECKING, Callable

from llpy import HttpServer, HttpRequest, HttpResponse, mc

if TYPE_CHECKING:
    from .handler import Handler


class APIHandler:
    def __init__(
        self, http_server: HttpServer, mc: mc, token: str, handler: "Handler"
    ) -> None:
        self.server = http_server
        self.mc = mc
        self.token = token
        self.handler = handler

        self.server.onGet("/llbds/_get_type", self._get_type)
        self.server.onGet("/llbds/_get_attr", self._get_attr)

    def is_authorized(self, request: HttpRequest) -> bool:
        return request.headers.get("Authorization")[0] == self.token

    def _get_type(self, request: HttpRequest, response: HttpResponse) -> None:
        # 鉴权
        if not self.is_authorized(request):
            response.status = 401
            response.reason = "Unauthorized"
            return None

        data = json.loads(request.params["content"])

        index: int = data["index"]
        name: str = data["name"]

        try:
            attr = getattr(self.handler.objects[index]["obj"], name)
        except AttributeError:
            response.status = 500
            response.reason = "Internal Server Error"
            return None

        if isinstance(attr, Callable):
            result = {"type": "function"}

        elif isinstance(attr, (str, int, float)):
            result = {"type": "value", "value": attr}
        else:
            # attr是LLSE对象
            result = {"type": "object"}

        response.write(json.dumps({"data": result}))
        response.status = 200
        response.reason = "OK"
        response.setHeader("Content-Type", "text/plain")

        return None

    def _get_attr(self, request: HttpRequest, response: HttpResponse) -> None:
        # 鉴权
        if not self.is_authorized(request):
            response.status = 401
            response.reason = "Unauthorized"
            return None

        data = json.loads(request.params["content"])

        index: str = data["index"]
        args: tuple = data["args"]
        kwargs: dict = data["kwargs"]

        try:
            attr = getattr(self.handler.objects[index]["obj"], data["attr"])
        except AttributeError:
            response.status = 500
            response.reason = "Internal Server Error"
            return None

        if isinstance(attr, Callable):
            # JSON格式化后，args会变为list
            result = attr(*tuple(args), **kwargs)

            if not isinstance(result, (str, int, float)):
                # 函数返回值是LLSE对象
                result = self.handler.handle({"obj": result, "event_name": None})[
                    "objects"
                ][0]
        elif isinstance(attr, (str, int, float)):
            result = attr
        else:
            # attr是LLSE对象
            result = self.handler.handle({"obj": attr, "event_name": None})["objects"][
                0
            ]

        response.write(json.dumps({"data": result}))
        response.status = 200
        response.reason = "OK"
        response.setHeader("Content-Type", "text/plain")

        return None
