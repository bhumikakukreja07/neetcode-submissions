class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, sol = [], []

        def backtrack(i):
            if i == len(s):
                res.append(sol.copy())
                return
            
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    sol.append(s[i:j+1])
                    backtrack(j + 1)
                    sol.pop()
        backtrack(0)
        return res