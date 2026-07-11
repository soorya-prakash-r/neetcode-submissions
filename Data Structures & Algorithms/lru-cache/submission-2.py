class Node:
    def __init__(self, k = 0, val = 0, next = None, prev = None):
        self.val = val
        self.key  = k
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.left = self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left
        self.c = capacity

    def get(self, key: int) -> int:
        if key in self.d.keys():
            t = self.d[key]
            self.remove(key)
            self.insert(key, t.val)
            return t.val

        return -1           
    
    def insert(self, k, v):
        temp = Node(k, v)
        prevn = self.right.prev
        prevn.next = temp
        temp.next = self.right
        self.right.prev = temp
        temp.prev = prevn
        self.d[k] = temp

    def remove(self, k):
        p = self.d[k]
        prevn, nextn = p.prev, p.next
        prevn.next = nextn
        nextn.prev = prevn
        del self.d[k]

    def put(self, key: int, value: int) -> None:
        if key in self.d.keys():
            self.remove(key)
            
        self.insert(key, value)
        if len(self.d.keys()) > self.c:
            self.remove(self.left.next.key)

        
