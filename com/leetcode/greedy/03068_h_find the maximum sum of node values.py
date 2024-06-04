from typing import List,Optional

class Solution:

    # num ^ k ^ k == num
    # We can actually XOR any two nodes that are connected in the graph, and XOR must be done in pairs
    # Calc diff = num ^ k - num, sort desc, add positive diff sum of pairs to result
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        diffs = [((num ^ k) - num) for num in nums]
        diffs.sort(reverse=True)
        res = sum(nums)     # Only apply XOR if it gives greater result
        for i in range(0, len(nums), 2):
            if i == len(nums) - 1:
                break
            diff = diffs[i] + diffs[i + 1]
            if diff <= 0:
                break
            res += diff
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testMinCameraCover(self):
        s = Solution()
        self.assertEqual(s.minCameraCover(TreeNode(0,TreeNode(0,TreeNode(0),TreeNode(0)))), 1)
        self.assertEqual(s.minCameraCover(TreeNode(0,TreeNode(0,TreeNode(0,TreeNode(0,None,TreeNode(0)))))), 2)
        


if __name__ == '__main__':
    unittest.main()