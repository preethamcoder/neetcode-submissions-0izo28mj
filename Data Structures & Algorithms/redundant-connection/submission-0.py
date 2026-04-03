class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [ind for ind in range(n+1)]
        ranks = [1]*(n+1)
        def find(node):
            res = node
            while res != parents[res]:
                parents[res] = parents[parents[res]]
                res = parents[res]
            return res
        # def find(node):
        #     if node != parents[node]:
        #         parents[node] = find(parents[node])
        #     return parents[node]
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            if p1 == p2:
                return False
            if ranks[p1] > ranks[p2]:
                parents[p2] = p1
                ranks[p1] += ranks[p2]
            else:
                parents[p1] = p2
                ranks[p2] += ranks[p1]
            return True
        for s, v in edges:
            if not union(s, v):
                return [s, v]
