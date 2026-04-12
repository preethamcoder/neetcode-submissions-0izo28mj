# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque([[root]])
        while q:
            curr = q.popleft()
            values = []
            next_values = []
            for node in curr:
                if node:
                    values.append(node.val)
                    if node.left:
                        next_values.append(node.left)
                    if node.right:
                        next_values.append(node.right)
            if values:
                res.append(values[-1])
            if next_values:
                q.append(next_values)
        return res