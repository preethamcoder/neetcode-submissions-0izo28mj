from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        length = len(tickets)
        res = ['JFK']
        graph = defaultdict(list)
        for s, v in tickets:
            graph[s].append(v)
        def dfs(src):
            if len(res) == length + 1:
                return res
            if src not in graph:
                return False
            tmp = graph[src]
            for ind, ver in enumerate(tmp):
                res.append(ver)
                graph[src].remove(ver)
                if dfs(ver):
                    return True
                res.pop()
                graph[src].insert(ind, ver)
            return False
        dfs('JFK')
        return res