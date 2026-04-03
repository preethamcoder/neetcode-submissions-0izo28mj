class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if l1 > l2:
            return False
        w1 = [0]*26
        for each in s1:
            w1[ord(each)-97] += 1
        for each in range(l2-l1+1):
            word = s2[each:each+l1]
            s2_char = [0]*26
            for char in word:
                s2_char[ord(char)-97] += 1
            if s2_char == w1:
                return True
        return False