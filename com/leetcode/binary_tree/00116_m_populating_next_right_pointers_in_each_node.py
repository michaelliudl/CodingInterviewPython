from typing import Optional,List,Deque


class Node:

    def __init__(self, val=0, left=None, right=None, next=None):
        self.val=val
        self.left=left
        self.right=right
        self.next=next
        

class Solution:

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        q=Deque()
        q.append(root)
        while q:
            size=len(q)
            prev=None
            for _ in range(size):
                cur=q.popleft()
                if not prev:
                    prev=cur
                else:
                    prev.next=cur
                prev=cur
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return root

    def connectRecur(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        self.connectChildren(root)
        return root
        
    def connectChildren(self, parent):
        if not parent:
            return
        pl,pr=parent.left,parent.right
        while pl and pr:
            pl.next=pr
            pl=pl.right
            pr=pr.left
        self.connectChildren(parent.left)
        self.connectChildren(parent.right)

import unittest

class TestSolution(unittest.TestCase):
    def testConnectRecur(self):
        s = Solution()
        root=Node(1,Node(2,Node(4),Node(5)),Node(3,Node(6),Node(7)))
        s.connectRecur(root)
        self.assertEqual(root.left.next.val, 3)
        self.assertEqual(root.left.left.next.val, 5)
        self.assertEqual(root.left.right.next.val, 6)

        self.assertEqual(s.connectRecur(None), None)


if __name__ == '__main__':
    unittest.main()