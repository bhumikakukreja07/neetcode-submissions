class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        group = list(range(len(edges) + 1))

        for a, b in edges:
            if group[a] == group[b]:
                return [a, b]

            newGrp = group[a]
            oldGrp = group[b]

            for i in range(len(group)):
                if group[i] == oldGrp:
                    group[i] = newGrp
        
        return []