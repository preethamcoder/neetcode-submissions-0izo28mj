"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 
        oldToNew = {}
        def clone(n):
            if n in oldToNew:
                return oldToNew[n]
            copy = Node(n.val)
            oldToNew[n] = copy
            for each in n.neighbors:
                copy.neighbors.append(clone(each))
            return copy
        return clone(node)