from collections import deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Make a graph and indegree dict
        # Indegree of 0 means that this is one of the first characters, and nothing needs to come before this
        graph = {c:set() for w in words for c in w}
        indegree = {c:0 for c in graph}
        length = len(words)
        # Build the graph and indegree dict
        for ind in range(length-1):
            w1 = words[ind]
            w2 = words[ind+1]
            l1, l2 = len(w1), len(w2)
            min_length = min(l1, l2)
            for each in range(min_length):
                if l1 > l2 and w1[:min_length] == w2[:min_length]:
                    return ""
                if w1[each] != w2[each]:
                    if w2[each] not in graph[w1[each]]:
                        graph[w1[each]].add(w2[each])
                        indegree[w2[each]] += 1
                    break
        # Fetch all the characters that the word could start with, ones with indegree of 0
        q = deque([c for c in indegree if indegree[c] == 0])
        res = []

        # Now pluck from the deque and build stuff
        while q:
            char = q.popleft()
            res.append(char)
            for each in graph[char]:
                indegree[each] -= 1
                if indegree[each] == 0:
                    q.append(each)
        if len(res) != len(indegree):
            return ''
        return ''.join(res)