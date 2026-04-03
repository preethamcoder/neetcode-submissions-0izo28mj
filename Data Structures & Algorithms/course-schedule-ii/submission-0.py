class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        course_map = {ind:[] for ind in range(numCourses)}
        for c, pr in prerequisites:
            course_map[c].append(pr)
        done = set()
        path = set()
        def dfs(course):
            if course in done:
                return True
            if course in path:
                return False
            path.add(course)
            for each in course_map[course]:
                if not dfs(each):
                    return False
            path.remove(course)
            done.add(course)
            res.append(course)
            return True
        for each in range(numCourses):
            if not dfs(each):
                return []
        return res