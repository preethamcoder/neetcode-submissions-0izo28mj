# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([[root]])
        while q:
            curr = q.popleft()
            values = []
            next_level = []
            for node in curr:
                if node:
                    values.append(node.val)
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
            if values:
                res.append(values)
            if next_level:
                q.append(next_level)
        return res