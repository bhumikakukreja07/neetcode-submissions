class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right, maxLen = 0, 0, 0
        hashmap = {}
        for right in range(len(s)):
            if s[right] in hashmap:
                hashmap[s[right]] += 1
            else:
                hashmap[s[right]] = 1
            if right != len(s):
                while ((right - left + 1) - max(hashmap.values() or [0])) > k:
                    hashmap[s[left]] -= 1
                    if hashmap[s[left]] == 0:
                        del hashmap[s[left]]
                    left += 1   
            maxLen = max(maxLen, right - left + 1)      
        return maxLen