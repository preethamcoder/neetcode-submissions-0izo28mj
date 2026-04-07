from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord or endWord not in wordList:
            return 0
        word_map = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for ind in range(len(word)):
                pattern = word[:ind] + '*' + word[ind+1:]
                word_map[pattern].append(word)
        seen = set([beginWord])
        res = 1
        q = deque([beginWord])
        while q:
            for ind in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for index in range(len(word)):
                    pattern = word[:index] + '*' + word[index+1:]
                    for each in word_map[pattern]:
                        if each not in seen:
                            seen.add(each)
                            q.append(each)
            res += 1
        return 0