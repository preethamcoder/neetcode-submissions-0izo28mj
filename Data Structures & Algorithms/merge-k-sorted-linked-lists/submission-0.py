# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_two(l1, l2):
            dummy = ListNode()
            h = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    dummy.next = l1
                    l1 = l1.next
                else:
                    dummy.next = l2
                    l2 = l2.next
                dummy = dummy.next
            dummy.next = l1 or l2
            return h.next
        if not lists:
            return
        length = len(lists)
        while len(lists) > 1:
            merged_lists = []
            for ind in range(0, len(lists), 2):
                list1 = lists[ind]
                list2 = lists[ind+1] if ind < len(lists)-1 else None
                merge = merge_two(list1, list2)
                merged_lists.append(merge)
            lists = merged_lists
        return lists[0]