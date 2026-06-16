class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([timestamp, value])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        pairs = self.hashmap[key]
        left, right = 0, len(pairs) - 1

        while left <= right:
            mid = (left + right) // 2

            if pairs[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1
        if right >= 0:
            return pairs[right][1]
        else:
            return ""