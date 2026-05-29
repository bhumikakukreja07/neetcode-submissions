class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l , r , count = 0 , 0 , 0
        hashset = set()

        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[r])
            count = max(count , len(hashset))
        return count