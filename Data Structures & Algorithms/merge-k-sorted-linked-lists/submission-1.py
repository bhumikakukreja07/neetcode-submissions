# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []

        for i in lists:
            while i:
                nodes.append(i.val)
                i = i.next
        nodes.sort()

        res = ListNode(0)
        cur = res

        for j in nodes:
            cur.next = ListNode(j)
            cur = cur.next
        return res.next