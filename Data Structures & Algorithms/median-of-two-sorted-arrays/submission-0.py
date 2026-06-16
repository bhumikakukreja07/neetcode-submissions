class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        c = nums1 + nums2
        c.sort()
        n = len(c)

        if n % 2 != 0:
            return c[n // 2]
        else:
            return (c[n // 2] + c[n // 2 - 1]) / 2.0