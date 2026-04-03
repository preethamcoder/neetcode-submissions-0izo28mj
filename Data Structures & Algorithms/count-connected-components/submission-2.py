class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [ind for ind in range(n)]
        ranks = [1]*n
        def find(node):
            res = node
            while res != parents[res]:
                parents[res] = parents[parents[res]]
                res = parents[res]
            return res
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            if p1 == p2:
                return 0
            if ranks[p1] >= ranks[p2]:
                parents[p2] = p1
                ranks[p1] += 1
            else:
                parents[p1] = p2
                ranks[p2] += 1
            return 1
        res = n
        for s, v in edges:
            res -= union(s, v)
        return res