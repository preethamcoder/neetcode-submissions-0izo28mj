from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord or endWord not in wordList:
            return 0
        wordList.append(beginWord)
        word_map = defaultdict(list)
        for word in wordList:
            for ind in range(len(word)):
                pattern = word[:ind] + '*' + word[ind+1:]
                word_map[pattern].append(word)
        seen = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for each in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for ind in range(len(word)):
                    pattern = word[:ind] + '*' + word[ind+1:]
                    for neighbor in word_map[pattern]:
                        if neighbor not in seen:
                            seen.add(neighbor)
                            q.append(neighbor)
            res += 1
        return 0