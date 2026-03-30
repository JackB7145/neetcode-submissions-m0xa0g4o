class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while stones and len(stones) > 1:
            print(stones)
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            print(first, second, stones)
            if first < second:
                heapq.heappush(stones, first - second)
            elif second < first:
                heapq.heappush(stones, second - first)
        

        return -stones[0] if stones else 0