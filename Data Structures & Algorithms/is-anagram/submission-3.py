class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = len(s)
        l2 = len(t)
        if l1 != l2:
            return False
        count = [0]*26
        for each in range(l1):
            count[ord(s[each])-97] += 1
            count[ord(t[each])-97] -= 1
        for each in count:
            if each != 0:
                return False
        return True