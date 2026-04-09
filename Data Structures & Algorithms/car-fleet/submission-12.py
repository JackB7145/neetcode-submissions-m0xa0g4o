class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''

    position[i] is the position of the ith car (in miles)
    speed[i] is the speed of the ith car (in miles per hour)

    You have a destination number of miles target

    If are a car catches up to a another one it's counted as 1 car

    The amount of time it takes for car[i] to get to destination is given by

    (target-position[i]) / speed[i] == how many units of time it'll to reach destination

        '''
    
        fleet = [(position[i], speed[i]) for i in range(len(position))]
        fleet.sort()
        stack = [] #Target: 10, 
        for start, speed in fleet:
            while stack and (target-start)/speed >= (target-stack[-1][0]/stack[-1][1]):
                stack.pop()
            stack.append((start, speed))
        return len(stack)-1




    