class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if l1 > l2:
            return False
        w1 = [0]*26
        w2 = [0]*26
        for each in range(l1):
            w1[ord(s1[each])-97] += 1
            w2[ord(s2[each])-97] += 1
        if w1 == w2:
            return True
        for ind in range(l1, l2):
            w2[ord(s2[ind])-97] += 1
            w2[ord(s2[ind-l1])-97] -= 1
            if w1 == w2:
                return True
        return False