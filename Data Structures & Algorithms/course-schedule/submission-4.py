from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = {ind:[] for ind in range(numCourses)}
        for c, pr in prerequisites:
            course_map[c].append(pr)
        seen = set()
        def dfs(course):
            if course_map[course] == []:
                return True
            if course in seen:
                return False
            seen.add(course)
            for each in course_map[course]:
                if not dfs(each):
                    return False
            seen.remove(course)
            #course_map[course] = []
            return True
        for ind in range(numCourses):
            if not dfs(ind):
                return False
        return True