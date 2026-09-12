class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        lets do some theory

        if we look at the example

        [1, 2, 3]

        we want to know the most efficient way to get to the top

        we can start on index 1 or 2, and jump 1 or two steps each time.

        in this case the answer is 2, because we start on step 1, and jump 2 to get to the top

        lets call the top T

        so we can get to T either by jumping 2 from T-2, or 1 from T-1

        T-2 = min(T-3, T-4)

        T-1 = min(T-2, T-3)

        so we can see this can be cached and memorized for a n solution and n space
        '''

        cache = {}

        def findMinimum(term):
            if term < 2:
                return cost[term]

            if term in cache:
                return cache[term]

            cache[term] = min(
                findMinimum(term - 2) + cost[term],
                findMinimum(term - 1) + cost[term]
            )

            return cache[term]

        n = len(cost)
        return min(findMinimum(n - 2), findMinimum(n - 1))

            