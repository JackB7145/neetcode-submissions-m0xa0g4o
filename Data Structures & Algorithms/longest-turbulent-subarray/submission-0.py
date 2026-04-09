class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        '''
        Maximum subarray with Kadahns Algorithm:

        you keep a global max and a local max

        where local max is the largest seen thus far

        this is just the largest seen thus far but conditionally 

        we can only make this check, 

        on the condition that the next value is the oposite, otherwise the local is reverterd

        to odd and we restart

        '''

        globalMax = 0
        localMax = 1
        even = True

        for i in range(1, len(arr)):
            if arr[i] % 2 == 0 and even or (arr[i] % 2 != 0 and not even):
                localMax += 1
                even = not even
            else:
                localMax = 1
                even = True

            globalMax = max(globalMax, localMax)
        
        return globalMax