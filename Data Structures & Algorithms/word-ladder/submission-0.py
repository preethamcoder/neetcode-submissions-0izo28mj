from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord or endWord not in wordList:
            return 0
        word_map = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for ind in range(len(word)):
                pattern = word[:ind] + "*" + word[ind+1:]
                word_map[pattern].append(word)
        seen = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for ind in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for ind in range(len(word)):
                    pattern = word[:ind] + '*' + word[ind+1:]
                    for w in word_map[pattern]:
                        if w not in seen:
                            seen.add(w)
                            q.append(w)
            res += 1
        return 0