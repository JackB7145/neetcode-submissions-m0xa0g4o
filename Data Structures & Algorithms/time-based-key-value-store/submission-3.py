class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        print(self.mp)
        values = self.mp[key]

        l, r = 0, len(values)-1
        res = ""

        while l <= r:
            m = (l+r)//2
            print(l, r, m)

            if values[m][0] == timestamp:
                return values[m][1]

            elif values[m][0] <= timestamp:
                res = values[m][1]
                l = m + 1

            else:
                r = m - 1

        return res
        
