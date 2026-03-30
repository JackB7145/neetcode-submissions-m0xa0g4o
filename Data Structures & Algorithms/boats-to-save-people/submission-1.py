class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
        Given an array people, where people[i] is the weight of the ith person

        We have a number of boats, where each boat can hold up to 2 people, or where

        the sum of the 2 people is equal to or less than limit

        such in an instance like

        [1, 2, 1]

        limit = 2

        the solution would be 2 boats with [1, 1], and [2]

        we need to determine the maximum number of boats to hold all the people

        basic strategy:

        group lightest people first. So sort, 

        and add the lightest people onto teh boat in pairs of 2 or until the lowest

        amount is done


        we know that each boat can hold 1 person, but can each boat hold 2 people in the question

        and instead of brute force for o(n^2) where we keep a grabbed array to skip, -> so 
        to grab all the lowest pairs first yk. 

        is sorting and going until we can't fit 2 people not the best?

        its an nlogn time complexity with a o(1) space complexity

        What do we know:

        1. Each boat can carry 2 or 1 people
        2. Each person can weigh up until 1 - limit

    
        Possible solution: 
        We could sort then do 2 pointer from left and right?


        [5, 1, 4, 2] limit 6

        [1, 2, 4, 5] 

            l  r

        res = 2

        [1, 3, 2, 3, 2] limit 3

        [1, 2, 2, 3, 3]
         l      r   

        res = 3     

        '''
        people.sort()
        l, r = 0, len(people)-1
        res = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                res += 1
                l += 1
                r -= 1
            else: 
                res += 1
                r -= 1


        return res
