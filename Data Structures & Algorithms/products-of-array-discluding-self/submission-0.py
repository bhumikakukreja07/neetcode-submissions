class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        countZero = 0
        ans = []
        for i in nums:
            if i == 0:
                countZero += 1
            product *= i
        for j in range(len(nums)):
            if countZero > 1:
                return [0] * len(nums)
            elif countZero == 1:
                product = 1
                for i in nums:
                    if i != 0:
                        product *= i
                        # ans.append(0)
                if nums[j] == 0:
                    ans.append(product)
                else:
                    ans.append(0)
            else:
                ans.append(product // nums[j])
        return ans