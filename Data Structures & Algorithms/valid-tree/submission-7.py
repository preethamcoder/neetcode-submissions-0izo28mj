class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph_map = {ind : [] for ind in range(n)}
        for s, v in edges:
            graph_map[s].append(v)
            graph_map[v].append(s)
        seen = set()
        def dfs(node, parent):
            if node in seen:
                return False
            seen.add(node)
            for each in graph_map[node]:
                if each == parent:
                    continue
                if not dfs(each, node):
                    return False
            return True
        return dfs(0, -1) and len(seen) == n