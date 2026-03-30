class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #You are given both the position and speed of the cars through an evenly indexed pair of arrays, position, and speed
        #A car fleet is 1 or a grouping of cars
        #There is a target number of miles
        #As each cars travel they may catch up to eachother resulting in a grouping. 
        #When 1 car catches up to the other, I need to get rid of that car or forget it from the array
        #Similar to the temperature question, however, I believe I'll use a monoatomic increasing array. 
        #I need to create a distance formula, factoring in the next cars speed and its position relative the target distance
        #If a car will make that distance in time, then it can be popped. Otherwise it should be added as a grouping in an array
        #Now I'm thinking its not going to be an array you pop from, it'll just be a stack you fill on the side and then count the length later
        fleet = []
        for i in range(len(position)):
            fleet.append((position[i], speed[i], (target - position[i])/speed[i]))
        
        fleet.sort(key=lambda a: a[0])

        groupings = []
        for pos, spee, hours in fleet:
            if not groupings:
                groupings.append((pos, spee, hours))
            else:
                while groupings and hours >= groupings[-1][2]:
                    groupings.pop()
                groupings.append((pos, spee, hours))
            print(groupings)

        return len(groupings)

            