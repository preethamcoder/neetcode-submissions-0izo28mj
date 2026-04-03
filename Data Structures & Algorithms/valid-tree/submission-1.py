class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        node_map = {ind:[] for ind in range(n)}
        for r, v in edges:
            node_map[r].append(v)
            node_map[v].append(r)
        seen = set()
        def dfs(n, parent):
            if n in seen:
                return False
            seen.add(n)
            for each in node_map[n]:
                if each == parent:
                    continue
                if not dfs(each, n):
                    return False
            return True
        return dfs(0, -1) and len(seen) == n