class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for a, b, time in times:
            graph[a].append((b, time))

        minTime = {}
        minHeap = [(0, k)]

        while minHeap:
            time_k_to_i , i = heapq.heappop(minHeap)

            if i in minTime:
                continue

            minTime[i] = time_k_to_i

            for nei, neiTime in graph[i]:
                if nei not in minTime:
                    heapq.heappush(minHeap, (time_k_to_i + neiTime, nei))

        if len(minTime) == n:
            return max(minTime.values())
        else:
            return -1