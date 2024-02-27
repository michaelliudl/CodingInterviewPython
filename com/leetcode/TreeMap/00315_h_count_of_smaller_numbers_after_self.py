from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.valCount = 1              # Count of `nums` elements equal to `val` in BST
        self.smallerCount = 0          # Count of `nums` elements less than `val`

class BinaryIndexedTree:
    def __init__(self, size=0):
        self.size = size
        self.tree = [0] * (size + 1)
    
    def query(self, index):
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= (index & -index)
        return result

    def update(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += (index & -index)

class Solution:

    # Use Binary Indexed Tree
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums: return []
        numsCopy = nums[:]
        numsCopy.sort()
        ranks = {num: i + 1 for i, num in enumerate(numsCopy)}
        n = len(nums)
        tree = BinaryIndexedTree(n)
        ans = [0] * n
        for i in range(n-1, -1, -1):
            num = nums[i]
            smallerCount = tree.query(ranks[num] - 1)
            ans[i] = smallerCount
            tree.update(ranks[num], 1)
        return ans


    # Still timeout. Use Binary Search Tree, last element in array is root
    def countSmallerBST(self, nums: List[int]) -> List[int]:

        def insertBST(node, val):
            if not node: return TreeNode(val)
            if val == node.val:
                node.valCount += 1
            elif val < node.val:
                node.left = insertBST(node.left, val)
                node.smallerCount += 1
            else:
                node.right = insertBST(node.right, val)
            return node
        
        def findSmaller(node, val):
            if not node: return 0
            if val == node.val:
                return node.smallerCount
            elif val < node.val:
                return findSmaller(node.left, val)
            else:
                smallerInRight = findSmaller(node.right, val)
                return node.smallerCount + node.valCount + smallerInRight   # All node value count and smaller count should be included

        if not nums: return []
        root = None
        ans = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):        # Iterate in reverse and insert each number as root to BST
            root = insertBST(root, nums[i])
            smaller = findSmaller(root, nums[i])
            ans[i] = smaller
        return ans

    # Modified merge sort
    def countSmallerMergeSort(self, nums: List[int]) -> List[int]:
        if not nums: return []
        pass

    # Brute
    def countSmallerBrute(self, nums: List[int]) -> List[int]:
        if not nums: return []
        n = len(nums)
        ans = [0] * n
        for i in range(n):
            for j in range(i+1, n):
                if nums[j] < nums[i]:
                    ans[i] += 1
        return ans



import unittest

class TestSolution(unittest.TestCase):
    def testCountSmaller(self):
        s = Solution()
        self.assertEqual(s.countSmaller(nums = [5,2,6,1]), [2,1,1,0])
        self.assertEqual(s.countSmaller(nums = [-1]), [0])
        self.assertEqual(s.countSmaller(nums = [-1,-1]), [0,0])


if __name__ == '__main__':
    unittest.main()