class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for each in strs:
            char_vec = [0]*26
            for char in each:
                char_vec[ord(char)-97] += 1
            char_vec = tuple(char_vec)
            if char_vec in words:
                words[char_vec].append(each)
            else:
                words[char_vec] = [each]
        return list(words.values())