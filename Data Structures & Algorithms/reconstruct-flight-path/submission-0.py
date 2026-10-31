class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for start, end in sorted(tickets, reverse = True):
            graph[start].append(end)

        route = []

        def dfs(city):
            while graph[city]:
                dfs(graph[city].pop())
                # use all the tickets out of this city

            route.append(city)
            # once all the tickets are finished from the city then add it to the route

        dfs("JFK")
        return route[::-1]