# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # break the chain

        curr = slow.next
        slow.next = None

        # reverse the second half

        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # combine

        h1 = head
        h2 = prev

        while h2:
            
            temp = h1.next
            h1.next = h2
            h1 = h2
            h2 = temp