import heapq
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        totalCost = 0
        seen = set()
        minHeap = [(0, 0)]

        while len(seen) < n:
            dist, i = heapq.heappop(minHeap)

            if i in seen:
                continue
            seen.add(i)
            totalCost += dist
            xi, yi = points[i]

            for j in range(n):
                if j not in seen:
                    xj, yj = points[j]
                    nei_dist = abs(xi-xj) + abs(yi-yj)
                    heapq.heappush(minHeap, (nei_dist, j))

        return totalCost