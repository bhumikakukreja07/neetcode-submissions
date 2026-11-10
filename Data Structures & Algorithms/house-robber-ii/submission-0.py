class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]

        skipFirstHouse = nums[1:]
        skipLastHouse = nums[:-1]

        lootSkippingFirst = self.robHelper(skipFirstHouse)
        lootSkippingLast = self.robHelper(skipLastHouse)

        return max(lootSkippingFirst, lootSkippingLast)

    def robHelper(self, array):
        if not array:
            return 0
        if len(array) == 1:
            return array[0]

        prev2 = array[0]
        prev1 = max(array[0], array[1])

        for i in range(2, len(array)):
            curr = max(prev1, prev2 + array[i])

            prev2 = prev1
            prev1 = curr

        return prev1