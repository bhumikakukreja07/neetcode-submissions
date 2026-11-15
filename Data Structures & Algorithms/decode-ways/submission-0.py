class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1                      # empty string: one way

        for i in range(1, n + 1):
            # one digit: s[i-1] must not be '0'
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            # two digits: s[i-2:i] must be 10..26
            if i >= 2 and 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[n]