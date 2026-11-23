class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        ''' 
        In a mountain array there are two regions

        1 region is increasing

        1 region is decreasing

        <Increasing> <Some idx i> <decreasing>

        But it seems the target coudld appear in both sides?

        So we need to find the pivot and then search both sides?

        We can binary search for the pivot, then binary search for the number in each section
        '''
        n = mountainArr.length()
        l, r = 0, n-2
        while l <= r:
            m = (l+r)//2
            if mountainArr.get(m) < mountainArr.get(m+1):
                l = m + 1
            else:
                r = m - 1

        pivot = l

        l, r = 0, pivot
        while l <= r:
            m = (l+r)//2
            ans = mountainArr.get(m)
            if ans == target:
                return m
            elif ans < target:
                l = m + 1
            else:
                r = m - 1
        
        l, r = pivot, n-1
        while l <= r:
            m = (l+r)//2
            ans = mountainArr.get(m)
            if ans == target:
                return m
            elif ans < target:
                r = m - 1
            else:
                l = m + 1

        return -1
            