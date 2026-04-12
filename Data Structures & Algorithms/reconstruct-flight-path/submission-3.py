from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for s, d in sorted(tickets, reverse=True):
            graph[s].append(d)
        path = ["JFK"]
        res = []
        while path:
            while graph[path[-1]]:
                path.append(graph[path[-1]].pop())
            res.append(path.pop())
        return res[::-1]