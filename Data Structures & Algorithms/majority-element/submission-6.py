class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = set()

        for i in nums:
            if i not in seen:
                seen.add(i)
                count = nums.count(i)
                if count > (len(nums)//2):
                    return i

        # return 2