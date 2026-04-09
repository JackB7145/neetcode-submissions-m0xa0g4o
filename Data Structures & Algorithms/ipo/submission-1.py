class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        '''
        We need to maximize profit while maintaining what possible capital we can use to achieve the profit

        If I have a profit W. I want the largest job at profit[i] where capital[i] <= W

        So first we start with W, we gather all of the capitals <= W. We then find the largest profit amongst those 

        I'm thinking a double heap solution, the minheap is used to moderate the capital, the maxheap is of size K, used to moderate the profit at each round

        then at the end, when the minheap is 0. We pop the remaining K elements and that's our profit?

        this could work

        this would be nlogn * logk
        '''

        minCapital = []
        maxProfit = []

        for i in range(len(capital)):
            heapq.heappush(minCapital, (capital[i], profits[i]))

        
        while minCapital or k:
            while minCapital and minCapital[0][0] <= w:
                heapq.heappush(maxProfit, -heapq.heappop(minCapital)[1])

            print(maxProfit)
            w += -heapq.heappop(maxProfit)
            k -= 1
        
        return w
