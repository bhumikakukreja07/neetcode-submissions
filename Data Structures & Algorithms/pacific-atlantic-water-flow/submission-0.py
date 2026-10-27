from collections import deque
class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows, cols = len(heights), len(heights[0])

        def bfs(queue, visited):
            while queue:
                row, col = queue.popleft()
                current = heights[row][col]

                # for cell below
                if row + 1 < rows and (row + 1, col) not in visited and heights[row + 1][col] >= current:
                    queue.append((row + 1, col))
                    visited.add((row + 1, col))

                # for cell above
                if row - 1 >= 0 and (row - 1, col) not in visited and heights[row - 1][col] >= current:
                    queue.append((row - 1, col))
                    visited.add((row - 1, col))

                # for right cell
                if col + 1 < cols and (row, col + 1) not in visited and heights[row][col + 1] >= current:
                    queue.append((row, col + 1))
                    visited.add((row, col + 1))

                # for left cell
                if col - 1 >= 0 and (row, col - 1) not in visited and heights[row][col - 1] >= current:
                    queue.append((row, col - 1))
                    visited.add((row, col - 1))

        # cells that can reach pacific
        pacificQueue = deque()
        visited1 = set()

        for c in range(cols):
            pacificQueue.append((0, c)) # top row
            visited1.add((0, c))
        for r in range(rows):
            pacificQueue.append((r, 0)) # left column
            visited1.add((r, 0))
        bfs(pacificQueue, visited1)

        # cells that can reach atlantic
        atlanticQueue = deque()
        visited2 = set()

        for c in range(cols):
            atlanticQueue.append((rows - 1, c)) # bottom row
            visited2.add((rows - 1, c))
        for r in range(rows):
            atlanticQueue.append((r, cols - 1)) # right column
            visited2.add((r, cols - 1))
        bfs(atlanticQueue, visited2)

        # cells in both oceans
        result = []

        for cell in visited1:
            if cell in visited2:
                result.append(list(cell))
        
        return result