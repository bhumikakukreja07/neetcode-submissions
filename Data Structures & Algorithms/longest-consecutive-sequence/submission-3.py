class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        maxLen = 0

        if not nums:
            return 0

        for i in sett:
            if i - 1 not in sett:
                curLen = 1
                cur = i
                maxLen = max(maxLen, curLen)
                
                while cur + 1 in sett:
                    curLen += 1
                    cur += 1
                    maxLen = max(maxLen, curLen)
        return maxLen