# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return None
        temp = head
        count = 1
        while temp.next:
            temp = temp.next
            count += 1
        temp = head
        k = count - n
        if k == 0:
            return head.next
        i = 0
        while temp:
            if i == k-1:
                temp.next = temp.next.next
                return head
            i += 1
            temp = temp.next



