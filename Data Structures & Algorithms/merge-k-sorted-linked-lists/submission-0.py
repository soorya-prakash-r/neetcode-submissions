# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return 

        while len(lists) > 1:
            print(len(lists))
            x = lists.pop()
            y = lists.pop()
            temp = self.mergelists(x,y)
            lists.append(temp)
        return lists[0]
    
    def mergelists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l2
        start = ListNode()

        if l1.val <= l2.val:
            start.val = l1.val
            l1 = l1.next
        else:
            start.val = l2.val
            l2 = l2.next
            
        head = start
        while l1 and l2:
            start.next = ListNode()
            if l1.val <= l2.val:
                start.next.val = l1.val
                l1 = l1.next
            else:
                start.next.val = l2.val
                l2 = l2.next
            start = start.next
        
        if l1:
            start.next = l1
        if l2:
            start.next = l2

        return head
