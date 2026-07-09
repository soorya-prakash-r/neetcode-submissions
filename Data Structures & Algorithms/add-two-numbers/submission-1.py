# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        head = l1
        x = 0
        x = l1.val + l2.val + x
        l1.val = x % 10
        x = x // 10
        while l1.next and l2.next:
            l1 = l1.next
            l2 = l2.next
            x = l1.val + l2.val + x
            l1.val = x % 10
            x = x // 10 

        while l2.next:
            l2 = l2.next
            l1.next = ListNode((l2.val + x)%10)
            x = (l2.val + x)// 10
            l1 = l1.next
        while l1.next:
            l1 = l1.next
            y = (l1.val + x)
            l1.val = y % 10
            x = y // 10
            print(x)
        if x > 0:
            l1.next = ListNode(x) 
        return head
