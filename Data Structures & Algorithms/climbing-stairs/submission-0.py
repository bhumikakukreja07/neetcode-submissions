class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2}

        def fibo(n):
            if n not in memo:
                memo[n] = fibo(n-2) + fibo(n-1)
            return memo[n]
        return fibo(n)