class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        l, r = 0, len(people)-1
        while l <= r:
            total = people[l] + people[r]
            if total <= limit:
                boats += 1
                l += 1
                r -= 1
            else:
                boats += 1
                r -= 1




        return boats