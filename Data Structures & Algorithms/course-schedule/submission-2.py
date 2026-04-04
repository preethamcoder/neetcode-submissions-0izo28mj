class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = {ind:[] for ind in range(numCourses)}
        for c, pr in prerequisites:
            course_map[c].append(pr)
        seen = set()
        def dfs(course):
            if course in seen:
                return False
            if course_map[course] == []:
                return True
            seen.add(course)
            for each in course_map[course]:
                if not dfs(each):
                    return False
            seen.remove(course)
            course_map[course] = []
            return True
        for each in range(numCourses):
            if not dfs(each):
                return False
        return True