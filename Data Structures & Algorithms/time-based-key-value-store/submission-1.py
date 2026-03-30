class TimeMap:

    '''
    We need a way to store by key, a list of timestamps and values
    We need a way to efficiently index them by grabbing the leftmost value to timestamp

    A hashamp that keeps track of an array of tuples at (timestamp, val) order

    When we set, we just append it onto the defualt dict

    When we get, we binary the search the strictly increasing array (By timestamp), and return the leftmost value
    '''

    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.mp[key]
        l, r = 0, len(arr)-1
        val = ""
        while l <= r:
            m = (l+r)//2
            if arr[m][0] <= timestamp:
                val = arr[m][1]
                l = m + 1
            else:
                r = m - 1
        return val
