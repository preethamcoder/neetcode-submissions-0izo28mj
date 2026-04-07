from collections import defaultdict
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord or endWord not in wordList:
            return 0
        res = 1
        word_map = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for ind in range(len(word)):
                pattern = word[:ind] + '*' + word[ind+1:]
                word_map[pattern].append(word)
        seen = set([beginWord])
        q = deque([beginWord])
        while q:
            for ind in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                #seen.add(word)
                for ind in range(len(word)):
                    pattern = word[:ind] + "*" + word[ind+1:]
                    for neighbor in word_map[pattern]:
                        if neighbor not in seen:
                            seen.add(neighbor)
                            q.append(neighbor)
            res += 1
        return 0