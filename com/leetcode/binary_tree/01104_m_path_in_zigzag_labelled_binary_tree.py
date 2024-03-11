from typing import List

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:

        def find(node, depth):
            ans.append(node)
            if node == 1 or depth == 0:
                return
            indexFromLeft = (2 ** depth - 1 - node) if depth % 2 == 0 else (node - 2 ** (depth - 1))
            indexParent = indexFromLeft // 2
            parentDepth = depth - 1
            parent = (2 ** parentDepth - 1 - indexParent) if parentDepth % 2 == 0 else (2 ** (parentDepth - 1) + indexParent)
            find(parent, parentDepth)

        labelDepth = 1
        while label > (2 ** labelDepth - 1):
            labelDepth += 1
        ans = []
        find(node = label, depth = labelDepth)
        ans.reverse()
        return ans

import unittest

class TestSolution(unittest.TestCase):
    def testPathInZigZagTree(self):
        s = Solution()
        self.assertEqual(s.pathInZigZagTree(label = 14), [1,3,4,14])
        self.assertEqual(s.pathInZigZagTree(label = 26), [1,2,6,10,26])



if __name__ == '__main__':
    unittest.main()