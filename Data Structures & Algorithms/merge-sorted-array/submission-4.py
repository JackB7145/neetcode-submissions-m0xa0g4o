class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = [m-1, n-1]

        for i in range(n+m-1, -1, -1):
            val1 = nums1[p1] if p1 > -1 else -10e9
            val2 = nums2[p2] if p2 > -1 else -10e9

            if val1 >= val2:
                p1 -= 1
            else:
                p2 -= 1
            
            nums1[i] = max(val1, val2)
        
