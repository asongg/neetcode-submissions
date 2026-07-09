class TimeMap:

    def __init__(self):
        self.timemap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key in self.timemap:
            values = self.timemap[key]
        else:
            return res
        l = 0
        r = len(values)-1
        while l <= r:
            mid = (r + l) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res
