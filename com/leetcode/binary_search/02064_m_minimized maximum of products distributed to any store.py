from typing import List

class Solution:

    # Binary search between 1 and the largest value in quantities
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        def countContainer(maxQ):
            return sum((((quant - 1) // maxQ) + 1) for quant in quantities)

        low = 1
        high = max(quantities)
        while low < high:
            mid = low + (high - low) // 2
            if countContainer(mid) <= n:
                high = mid
            else:
                low = mid + 1
        return low


import unittest

class TestSolution(unittest.TestCase):
    def testSearch(self):
        s = Solution()
        self.assertEqual(s.search([1], 1), 0)
        self.assertEqual(s.search([4,5,6,7,0,1,2], 0), 4)



if __name__ == '__main__':
    unittest.main()