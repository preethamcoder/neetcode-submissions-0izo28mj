class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(':')', '{':'}', '[':']'}
        stack = []
        for each in s:
            if each in pairs:
                stack.append(each)
            else:
                if not stack:
                    return False
                elem = stack.pop()
                if each != pairs[elem]:
                    return False
        return not stack