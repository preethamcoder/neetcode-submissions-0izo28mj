class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        course_map = {ind:[] for ind in range(n)}
        for s, v in edges:
            course_map[s].append(v)
            course_map[v].append(s)
        seen = set()
        def dfs(node, parent):
            if node in seen:
                return False
            seen.add(node)
            for each in course_map[node]:
                if each == parent:
                    continue
                if not dfs(each, node):
                    return False
            return True
        return dfs(0, -1) and len(seen) == n