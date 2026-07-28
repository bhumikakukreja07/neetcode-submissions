class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, sol, total):
            if total == target:
                res.append(sol.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            # If we pick
            sol.append(candidates[i])
            backtrack(i + 1, sol, total + candidates[i])
            sol.pop()

            # If we don't pick
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, sol, total)
        
        backtrack(0, [], 0)
        return res