import time
from sys import maxsize


class Handler:
    def __init__(self, timeout: int = 60):
        self.objects = {}
        self.timeout = timeout
        self._idx = 0
        self._maxsize = maxsize // 2

    @property
    def idx(self):
        self._idx = self._idx % self._maxsize
        return self._idx

    def handle(self, data: dict):
        result = []
        direct_data = []
        for key, obj in data.items():
            if key != "event_name" or not isinstance(obj, (str, int, float)):
                self.objects[self.idx] = {"obj": obj, "time": int(time.time())}

                if hasattr(obj, "name"):
                    result.append({"type": key, "index": self.idx, "name": getattr(obj, "name")})
                else:
                    result.append({"type": key, "index": self.idx})
                self._idx += 1

            if isinstance(obj, (str, int, float)) or obj is None:
                direct_data.append({"type": key, "value": obj})
        return {
            "event_name": data["event_name"],
            "objects": result,
            "direct_data": direct_data,
        }

    def clear_timeouted_objects(self):
        keys_to_remove = []
        current_time = time.time()

        for key, obj in self.objects.items():
            if obj["time"] + self.timeout < current_time:
                keys_to_remove.append(key)

        for key in keys_to_remove:
            self.objects.pop(key)
