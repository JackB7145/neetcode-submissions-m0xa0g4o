class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        You have two costs always, the cost of taking the i-1 step, and the cost of taking 
        the i-2 step. One is the older one used for storage whearas two is the one that makes the best calculations


        If Im trying to reach floor n

        I need to do the minimum cost between n-1, and n-2

        so you can also say that 

        one = n
        two = n + 1
        three = min(one+cost(three), two+cost(three))

        one = two
        two = three
        
        
        
        '''

        one = cost[0]
        two = cost[1]
        for i in range(3, len(cost)):
            new = min(one+cost[i], two+cost[i])
            one = two
            two = new
        
        return two
            
        
        