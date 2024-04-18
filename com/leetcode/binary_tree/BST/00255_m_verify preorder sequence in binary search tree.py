from typing import Optional,List,Deque
import math

'''
Given an array of unique integers preorder, return true if it is the correct preorder traversal sequence of a binary search tree.

'''

class Solution:

    # Use scanned part of original array as stack
    def verifyPreorder(self, preorder: List[int]) -> bool:
        low = -math.inf
        index = -1
        for num in preorder:
            if num < low:
                return False
            while index >= 0 and preorder[index] < num:
                low = preorder[index]
                index -= 1
            index += 1
            preorder[index] = num
        return True

    # Monotonic stack to track low value
    def verifyPreorderStack(self, preorder: List[int]) -> bool:
        low = -math.inf
        stack = []

        for num in preorder:
            if num < low:
                return False
            while stack and stack[-1] < num:
                low = stack.pop()
            stack.append(num)
        return True

    # DFS with low/high bounds
    def verifyPreorderDFS(self, preorder: List[int]) -> bool:
        
        def dfs(low, high):
            nonlocal index
            if index == len(preorder):
                return
            cur = preorder[index]
            if cur < low or cur > high:
                return
            index += 1
            dfs(low, cur)
            dfs(cur, high)

        if not preorder:
            return False
        index = 0
        dfs(low = -math.inf, high = math.inf)
        return index == len(preorder)


import unittest

class TestSolution(unittest.TestCase):
    def testVerifyPreorder(self):
        s = Solution()
        self.assertEqual(s.verifyPreorder(preorder = [5,2,1,3,6]), True)
        self.assertEqual(s.verifyPreorder(preorder = [5,2,6,1,3]), False)
        
if __name__ == '__main__':
    unittest.main()