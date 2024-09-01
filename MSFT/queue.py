class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

# Implement a queue with capacity limit and `delete_all` and `copy` functions
class Queue:

    def __init__(self, cap = 0):
        if cap <= 0:
            raise('Cap should be >= 0')
        self.cap = cap
        self.total = 0
        self.head = None
        self.tail = None

    def push(self, value):
        if self.total == self.cap:
            raise('Queue is at cap ' + str(self.cap))
        node = ListNode(value)
        if not self.head:
            self.head = node
        if not self.tail:
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.total += 1
    
    def pop(self):
        if not self.head:
            raise('Queue is empty')
        node = self.head
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.total -= 1
        return node.val

    def count(self):
        return self.total
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.total = 0

    def copy(self):
        if not self.head or not self.tail:
            return None
        newQueue = Queue(self.cap)
        node = self.head
        while node:
            newQueue.push(node.val)
            node = node.next
        return newQueue
