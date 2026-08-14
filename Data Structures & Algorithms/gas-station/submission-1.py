class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        '''
        What makes the start invalid?

        When there is a point where the tank has -1 gas

        so I need to find the starting place where there isn't a point of -ve gas on the path forward

        we first check if it is possible

        if it is then we work our way through seeing how where to start

        its not possible for the start to have a -ve benefit so we can skip those

        and then we keep track of a running counter, when it dips below zero

        the next starting point could be anywhere after the first detected negative

        but when we find it to be -1. doesn't that mean the answer can't be anwhere from start to current

        yeah thats true actually, assuming we start on a positive, we can't have anything between start and the end


        '''
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1

        benefit = [gas - cost for gas, cost in zip(gas, cost)]
        
        start = 0
        cnt = 0

        for i in range(len(benefit)):
            if cnt < 0 and benefit[i] > 0:
                start = i
                cnt = 0

            cnt += benefit[i]

        return start
        

