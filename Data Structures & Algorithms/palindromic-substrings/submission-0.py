class Solution:
    def countSubstrings(self, s: str) -> int:
        resLen = 0

        for i in range(len(s)):
            # Odd len
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                resLen += 1
                l -= 1
                r += 1
            
            # Even len
            l, r = i, i + 1
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                resLen += 1
                l -= 1
                r += 1
        return resLen