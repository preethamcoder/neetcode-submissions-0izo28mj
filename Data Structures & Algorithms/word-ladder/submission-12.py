from collections import deque
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord or endWord not in wordList:
            return 0
        wordList.append(beginWord)
        words = defaultdict(list)
        res = 1
        for word in wordList:
            for ind in range(len(word)):
                pattern = word[:ind] + '*' + word[ind+1:]
                words[pattern].append(word)
        seen = set()
        q = deque([beginWord])
        while q:
            for ind in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return res
                if w in seen:
                    continue
                seen.add(w)
                for each in range(len(w)):
                    pattern = w[:each] + '*' + w[each+1:]
                    for word in words[pattern]:
                        if word not in seen:
                            q.append(word)
            res += 1
        return 0