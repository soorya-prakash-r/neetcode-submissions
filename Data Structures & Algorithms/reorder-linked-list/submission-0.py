# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        temp = slow.next
        slow.next = None
        x =  None
        while temp:
            t = temp.next
            temp.next = x
            x = temp
            temp = t

        fast = x
        start = head
        while fast and start:
            t = start.next
            start.next = fast
            fast = fast.next
            start.next.next = t
            start = start.next.next
        
        

