class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        seen = {(0, 0)}

        def push(time, row, col):
            if 0 <= row < n and 0 <= col < n and (row, col) not in seen:
                seen.add((row, col))
                heapq.heappush(heap, (max(time, grid[row][col]), row, col))

        while heap:
            time, row, col = heapq.heappop(heap)

            if row == n - 1 and col == n - 1:
                return time

            push(time, row + 1, col)
            push(time, row - 1, col)
            push(time, row, col + 1)
            push(time, row, col - 1)

        return - 1