class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxA = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:
                return 0

            grid[row][col] = 0
            
            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    maxA = max(maxA, dfs(row, col))
        
        return maxA