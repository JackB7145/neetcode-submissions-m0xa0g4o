class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        '''
        kokos eating banaas but with boxes.

        The maximum capacity we can choose is the sum of all the boxes

        the smallest is 1

        than your while loop, and counting mechanism to count how many days it takes

        '''

        l, r = max(weights), sum(weights)

        while l <= r:
            capacity = (l+r)//2
            print(f'\tCapacity {capacity} = {l}+{r}//2')
            count = 0
            day = 1
            for weight in weights:
                count += weight
                if count > capacity:
                    day += 1
                    count = weight
                
                print(f'Weight {weight}')
                print(f'Count {count}')
                print(f'Days {day}')

            if day <= days:
                r = capacity - 1
                res = capacity
            else:
                l = capacity + 1
        
        return res