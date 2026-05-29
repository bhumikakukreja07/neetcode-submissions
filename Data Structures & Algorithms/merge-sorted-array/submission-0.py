class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr1P, arr2P = len(nums1)-1 , 0

        while nums1[arr1P] == 0:
            nums1[arr1P] = nums2[arr2P]
            arr1P -= 1
            arr2P += 1

        nums1.sort()