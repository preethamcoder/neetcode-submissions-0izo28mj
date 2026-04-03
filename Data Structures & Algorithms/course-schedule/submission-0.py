class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = {ind:[] for ind in range(numCourses)}
        for each in prerequisites:
            course_map[each[0]].append(each[1])
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
            course_map[course] = []
            return True
        for each in range(numCourses):
            if not dfs(each):
                return False
        return True