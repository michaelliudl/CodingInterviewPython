from typing import Optional
from typing import List
from typing import Deque

class Node:
    def __init__(self, val=0, children=None):
        self.val=val
        self.children=children

class Solution:

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        r=[]
        q=Deque()
        q.append(root)
        while q:
            size=len(q)
            r1=[]
            for _ in range(size):
                n=q.popleft()
                r1.append(n.val)
                if n.children:
                    for c in n.children:
                        q.append(c)
            r.append(r1)
        return r
    

import unittest

class TestSolution(unittest.TestCase):
    def testLevelOrder(self):
        s = Solution()
        self.assertEqual(s.levelOrder(Node(1,[Node(3,[Node(5),Node(6)]),Node(2),Node(4)])), [[1],[3,2,4],[5,6]])
        self.assertEqual(s.levelOrder(Node(1,[Node(2),Node(3,[Node(6),Node(7,[Node(11,[Node(14)])])]),Node(4,[Node(8,[Node(12)])]),Node(5,[Node(9,[Node(13)]),Node(10)])])), 
                         [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]])
        self.assertEqual(s.levelOrder(None), [])


if __name__ == '__main__':
    unittest.main()