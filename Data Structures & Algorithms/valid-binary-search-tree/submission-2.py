# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        res = []
        def in_ord(r):
            if not r:
                return 
            in_ord(r.left)
            res.append(r.val)
            in_ord(r.right)
        in_ord(root)
        length = len(res)
        for ind in range(length - 1):
            if res[ind] >= res[ind+1]:
                return False
        return True