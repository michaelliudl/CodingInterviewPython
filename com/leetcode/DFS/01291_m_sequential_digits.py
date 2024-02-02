from typing import List

class Solution:

    def sequentialDigits(self, low: int, high: int) -> List[int]:

        def dfs(start, digit):
            if digit>=low and digit<=high:
                ans.append(digit)
            if digit>high or start==10:
                return
            nextDigit = digit * 10 + start
            dfs(start + 1, nextDigit)


        if low<=0 or high<=0 or low>=high: return []
        ans=[]
        for i in range(1,10):
            dfs(start=i, digit=0)
        ans.sort()
        return ans


        

import unittest

class TestSolution(unittest.TestCase):

    def testSequentialDigits(self):
        s = Solution()
        self.assertEqual(s.sequentialDigits(low = 100, high = 300), [123,234])
        self.assertEqual(s.sequentialDigits(low = 1000, high = 13000), [1234,2345,3456,4567,5678,6789,12345])

if __name__ == '__main__':
    unittest.main()