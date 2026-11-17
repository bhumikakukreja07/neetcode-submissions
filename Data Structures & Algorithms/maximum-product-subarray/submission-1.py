class Solution:
    def maxProduct(self, nums):
        current_max = nums[0]
        current_min = nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]

            if x < 0:
                current_max, current_min = current_min, current_max

            current_max = max(x, x * current_max)
            current_min = min(x, x * current_min)

            answer = max(answer, current_max)

        return answer