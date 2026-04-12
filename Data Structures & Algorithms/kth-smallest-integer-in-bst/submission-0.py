# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return []
        heap = []
        def in_ord(r):
            if not r:
                return
            in_ord(r.left)
            if len(heap) == k:
                heapq.heappushpop(heap, -1*r.val)
            else:
                heapq.heappush(heap, -1*r.val)
            in_ord(r.right)
        in_ord(root)
        elem = heapq.heappop(heap)
        return -1*elem