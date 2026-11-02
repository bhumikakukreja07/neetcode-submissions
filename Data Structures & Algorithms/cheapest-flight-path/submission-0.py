class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for num in range(k + 1):
            newPrices = prices.copy()

            for fromm, to, cost in flights:
                if prices[fromm] == float('inf'):
                    continue
                if prices[fromm] + cost < newPrices[to]:
                    newPrices[to] = prices[fromm] + cost

            prices = newPrices
        
        if prices[dst] == float('inf'):
            return -1
        else:
            return prices[dst]