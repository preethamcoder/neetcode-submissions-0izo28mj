class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = len(s)
        l2 = len(t)
        if l1 != l2:
            return False
        else:
            chars = {}
            for each in s:
                if each in chars:
                    chars[each] += 1
                else:
                    chars[each] = 1
            for each in t:
                if each not in chars or chars[each] == 0:
                    return False
                else:
                    chars[each] -= 1
            return True