class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        We have to return the number of subarrays that equal to the sum of k.

        At the first point, we have 2. We know 2 is k, so we increase the count

        then we hit -1 and we are at 1, i feel like this is a backtracking question?

        since we essentially are choosing at each point to continue using the same index start, or not. 
        and if we, at any point equal k we increment our count.

        I feel like I don't have another option for these reasons:

        1. I can't sort given that I have to count subbarrays which maintain order
        2. Since I can't sort, there is no way of knowing whether I should greedily move my start over, and continue or keep it there. 

        I don't need backtracking, lets jsut do it iteratively? with O(N^2) which is the fucking solution since nums.length is 1 - 20000

        I guess my next consideration is why would I do this with recursion. I don't have to worry about duplicates. The solution is quite simple

        hmmmm
        '''
        res = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    print('increasing total', i, j)
                    res += 1
        return res


