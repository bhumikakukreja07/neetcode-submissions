class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, sol, total):
            if total == target:
                res.append(sol.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            # If we pick
            sol.append(nums[i])
            backtrack(i, sol, total + nums[i])
            sol.pop()

            # If we don't pick
            backtrack(i + 1, sol, total)
        
        backtrack(0, [], 0)
        return res