class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            fst = heapq.heappop(stones)
            sec = heapq.heappop(stones)

            if sec > fst:
                heapq.heappush(stones, fst - sec)
        heapq.heappush(stones, 0)
        print(stones)
        return abs(stones[0])