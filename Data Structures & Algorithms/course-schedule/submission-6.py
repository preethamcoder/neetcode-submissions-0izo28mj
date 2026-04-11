class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {ind:[] for ind in range(numCourses)}
        for c, pr in prerequisites:
            graph[c].append(pr)
        seen = set()
        def dfs(course):
            if graph[course] == []:
                return True
            if course in seen:
                return False
            seen.add(course)
            for each in graph[course]:
                if not dfs(each):
                    return False
            graph[course] = []
            return True
        for ind in range(numCourses):
            if not dfs(ind):
                return False
        return True