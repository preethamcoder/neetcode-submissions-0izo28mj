# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        tmp = root
        if not tmp:
            return
        tmp.left, tmp.right = tmp.right, tmp.left
        self.invertTree(tmp.left)
        self.invertTree(tmp.right)
        return root