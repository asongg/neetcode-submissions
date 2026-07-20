# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        second = prev
        i = 1
        while i < n:
            curr = prev
            prev = prev.next
            i += 1
        if not curr:
            second = prev.next
        else:
            curr.next = prev.next
        fin = None
        while second:
            temp = second.next
            second.next = fin
            fin = second
            second = temp
        return fin
        