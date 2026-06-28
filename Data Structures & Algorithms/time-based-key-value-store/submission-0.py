class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return ""
        
        res = ""
        arr = self.storage[key]
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if arr[m][1] <= timestamp:
                res = arr[m][0]
                l = m + 1
            else:
                r = m - 1
        return res 
            
        
