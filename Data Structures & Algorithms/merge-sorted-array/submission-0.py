class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        '''
        You are given 2 sorted arrays in increasing order

        Nums1 will always be n+m in size. We need to return the sorted array

        The inefficient solution he is to append them, remove the zeros, and sort. Thats O(m) *nlog(n), very inefficient

        we need to do this in place

        at o(n) time complexity

        we could load an with a maximum space of m

        we could do it n log(m) with a heap

        what if we looked at it in the oposite light. What if we wanted to do largest, right to left 

        start at n + m, iterate from n backwards and m in the other array

        marker = n + m
        startBig = n
        startSmall = m

        compare the two biggest numbers

        the larger is placed in the marker (Which then decreases by 1)

        The unplaced remains, and the other one progresses



        '''

        marker = n + m - 1
        nMarker = m - 1
        mMarker = n - 1
        while marker > -1:
            val1 = nums1[nMarker] if nMarker > -1 else None
            val2 = nums2[mMarker] if mMarker > -1 else None

            if val1 and (not val2 or val1 > val2):
                nums1[marker] = val1
                nMarker -= 1
            else:
                nums1[marker] = val2
                mMarker -= 1
            
            marker -= 1
            
        