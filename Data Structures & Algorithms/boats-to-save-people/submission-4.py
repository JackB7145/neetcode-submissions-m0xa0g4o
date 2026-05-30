class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l, r = 0, len(people)-1

        people.sort()

        res = 0
        while l <= r:
            total = people[l] + people[r] if l != r else people[l]

            while r > 0 and total > limit:
                res += 1
                r -= 1
                total = people[l] + people[r]

            res += 1

            l += 1
            r -= 1
                
        return res





