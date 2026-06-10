class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []

        for i in range(len(nums) - k + 1):
            windowMax = max(nums[i:k+i])
            ans.append(windowMax)
        return ans