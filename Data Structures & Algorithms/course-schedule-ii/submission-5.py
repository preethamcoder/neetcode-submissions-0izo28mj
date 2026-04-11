class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        graph = {ind:[] for ind in range(numCourses)}
        for c, pr in prerequisites:
            graph[c].append(pr)
        done = set()
        path = set()
        def dfs(course):
            if course in path:
                return False
            if course in done:
                return True
            path.add(course)
            for each in graph[course]:
                if not dfs(each):
                    return False
            path.remove(course)
            done.add(course)
            res.append(course)
            return True
        for ind in range(numCourses):
            if not dfs(ind):
                return []
        return res