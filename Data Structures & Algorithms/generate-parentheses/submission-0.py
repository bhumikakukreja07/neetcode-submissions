class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, sol = [], []

        def backtrack(open, close):
            if open < n:
                # open is possible, let's try
                sol.append('(')
                backtrack(open + 1, close)
                sol.pop()
            if open > close:
                # closing in possible, let's try
                sol.append(')')
                backtrack(open, close + 1)
                sol.pop()
            if open == close == n:
                res.append(''.join(sol))
        backtrack(0, 0)
        return res