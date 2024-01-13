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
        
        def recur(left: Node, right: Node, prev: Node):
            if not left and not right:
                return
            nextCurLevel=None
            if prev:
                p=prev
                while p.next:
                    if not p.next.left and not p.next.right:
                        p=p.next
                    else:
                        nextCurLevel=p.next.left if p.next.left else p.next.right
                        break

            if left:
                left.next=right if right else nextCurLevel
            if right:
                right.next=nextCurLevel
            if left:
                recur(left.left, left.right, prev=left)
            if right:
                recur(right.left, right.right, prev=right)

        recur(root.left, root.right, prev=root)
        return root

import unittest

class TestSolution(unittest.TestCase):
    def testConnect(self):
        s = Solution()
        # root=Node(1,Node(2,Node(4),Node(5)),Node(3,None,Node(7)))
        # s.connect(root)
        # self.assertEqual(root.left.next.val, 3)
        # self.assertEqual(root.left.left.next.val, 5)
        # self.assertEqual(root.left.right.next.val, 7)

        # root=Node(1,Node(2,Node(4,Node(7)),Node(5)),Node(3,None,Node(6,None,Node(8))))
        # s.connect(root)
        # self.assertEqual(root.left.left.left.next.val, 8)

        root=Node(2,Node(1,Node(0,Node(2)),Node(7,Node(1),Node(0,Node(7)))),Node(3,Node(9),Node(1,Node(8),Node(8))))
        s.connect(root)
        self.assertEqual(root.left.right.next.val, 9)
        self.assertEqual(root.left.right.next.next.val, 1)
        self.assertEqual(root.left.right.right.next.val, 8)
        self.assertEqual(root.left.right.right.next.next.val, 8)

        self.assertEqual(s.connect(None), None)


if __name__ == '__main__':
    unittest.main()