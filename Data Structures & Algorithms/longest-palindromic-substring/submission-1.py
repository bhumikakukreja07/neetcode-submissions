class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start, best = 0, 1

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j] and (length <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    
                    if length > best:
                        best = length
                        start = i

        return s[start: start + best]