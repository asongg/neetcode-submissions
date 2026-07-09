# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        size = 0
        while curr:
            curr = curr.next
            size += 1

        curr = head
        i = 0
        while i < (size - n) - 1:
            i += 1
            curr = curr.next
        if size - n == 0:
            curr = curr.next
            return curr
        curr.next = curr.next.next
        return head

        