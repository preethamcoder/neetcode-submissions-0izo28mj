class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cmap = {ind:[] for ind in range(numCourses)}
        for c, pr in prerequisites:
            cmap[c].append(pr)
        seen = set()
        def dfs(crse):
            if cmap[crse] == []:
                return True
            if crse in seen:
                return False
            seen.add(crse)
            for each in cmap[crse]:
                if not dfs(each):
                    return False
            cmap[crse] = []
            seen.remove(crse)
            return True
        for each in range(numCourses):
            if not dfs(each):
                return False
        return True
            