# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        temp = None
        end = None
        while head and head.next: 
            temp = head.next
            head.next = end
            end = head
            head = temp
        if head:
            head.next = end
        return head
