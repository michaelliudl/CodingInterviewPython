from typing import List, Deque, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # Find subtree roots that match head, then find children match subsequent list nodes
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return
            if node.val == head.val:
                treeNodes.append(node)
            dfs(node.left)
            dfs(node.right)

        treeNodes = Deque()
        dfs(node=root)
        cur = head
        while cur:
            if not treeNodes:
                return False
            curLen = len(treeNodes)
            for _ in range(curLen):
                node = treeNodes.popleft()
                if cur.next:
                    if node.left and node.left.val == cur.next.val:
                        treeNodes.append(node.left)
                    if node.right and node.right.val == cur.next.val:
                        treeNodes.append(node.right)
            cur = cur.next
        return True

import unittest

class TestSolution(unittest.TestCase):
    def testDeckRevealedIncreasing(self):
        s = Solution()
        self.assertEqual(s.deckRevealedIncreasing(deck = [17,13,11,2,3,5,7]), [2,13,3,11,5,17,7])
        self.assertEqual(s.deckRevealedIncreasing(deck = [1,1000]), [1,1000])


if __name__ == '__main__':
    unittest.main()