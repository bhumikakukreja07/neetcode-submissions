class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for prefix in range(1, n + 1):
            for w in wordDict:
                L = len(w)

                if L <= prefix and dp[prefix - L]                            and s[prefix - L: prefix] == w:
                    dp[prefix] = True
                    break
        return dp[n]