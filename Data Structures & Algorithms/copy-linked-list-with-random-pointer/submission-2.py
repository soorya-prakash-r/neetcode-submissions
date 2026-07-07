"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {}
        temp = head
        while temp:
            new = Node(temp.val)
            d[temp] = new
            temp = temp.next

        temp = head
        while temp:
            newhead = d[temp]
            newhead.val = d[temp].val
            newhead.next = d.get(temp.next, None)
            newhead.random = d.get(temp.random, None)
            temp = temp.next

        return d.get(head, None)