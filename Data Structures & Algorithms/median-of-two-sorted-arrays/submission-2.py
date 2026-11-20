class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def kth(k):
            # k-th smallest (0-indexed) of nums1 + nums2
            l1, r1 = 0, len(nums1) - 1
            l2, r2 = 0, len(nums2) - 1

            while l1 <= r1 and l2 <= r2:
                m1 = (l1 + r1) // 2
                m2 = (l2 + r2) // 2
                numbersToLeft = m1 + m2

                if numbersToLeft >= k:
                    # too far right: drop the larger mid and everything after it
                    if nums1[m1] < nums2[m2]:
                        r2 = m2 - 1
                    else:
                        r1 = m1 - 1
                else:
                    # too far left: drop the smaller mid and everything before it
                    if nums1[m1] < nums2[m2]:
                        l1 = m1 + 1
                    else:
                        l2 = m2 + 1

            # one array is used up, so the answer is in the other one
            if l1 > r1:
                return nums2[k - l1]
            return nums1[k - l2]

        totalNumbers = len(nums1) + len(nums2)
        medianIdx = totalNumbers // 2
        if totalNumbers % 2:
            return float(kth(medianIdx))
        return (kth(medianIdx - 1) + kth(medianIdx)) / 2