from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
        
        def rotByBFS(r, c):
            nonlocal fresh
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                grid[r][c] = 2
                fresh -= 1
                queue.append((r, c))

        minute = 0

        while queue and fresh > 0:
            minute += 1

            for _ in range(len(queue)):
                row, col = queue.popleft()
                rotByBFS(row + 1, col)
                rotByBFS(row - 1, col)
                rotByBFS(row, col + 1)
                rotByBFS(row, col - 1)

        return minute if fresh == 0 else -1