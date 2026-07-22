class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        start = []
        end = []

        for cnt, f, t in trips:
            start.append((f, cnt))
            end.append((t, cnt))

        start.sort()
        end.sort()

        idx = 0

        passengers = 0

        print(start)

        print(end)

        for strt, newPassengers in start:
            passengers += newPassengers

            print(passengers)
            while idx < len(end) and end[idx][0] <= strt:
                passengers -= end[idx][1]
                idx += 1

            print(passengers)

            if passengers > capacity:
                return False
        
        return True