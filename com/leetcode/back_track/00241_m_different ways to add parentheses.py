from typing import List

class Solution:

    # Not really adding parenthese, just evaluate expression before and after each operator
    def diffWaysToCompute(self, expression: str) -> List[int]:

        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
        }
        
        def backtrack(left, right):
            res = []
            for i in range(left, right + 1):
                op = expression[i]
                if op in operations:
                    nums1 = backtrack(left, i - 1)
                    nums2 = backtrack(i + 1, right)
                    for num1 in nums1:
                        for num2 in nums2:
                            res.append(operations[op](num1, num2))
            # No operator in range, convert substring to number
            if not res:
                res.append(int(expression[left : right + 1]))
            return res
        
        return backtrack(0, len(expression) - 1)

import unittest

class TestSolution(unittest.TestCase):
    def testSubsets(self):
        s = Solution()
        self.assertEqual(s.subsets(nums = [1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertEqual(s.subsets(nums = [0]), [[],[0]])
        


if __name__ == '__main__':
    unittest.main()