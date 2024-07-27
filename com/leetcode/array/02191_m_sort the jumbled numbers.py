from typing import List

class Solution:

    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        def mapp(num):
            if num == 0:            # Input can be 0
                return mapping[0]
            res = 0
            multiplier = 1
            while num:
                res += (mapping[num % 10] * multiplier)
                num //= 10
                multiplier *= 10
            return res

        mapped = [(mapp(num), index, num) for index, num in enumerate(nums)]
        mapped.sort()
        return [num for _, _, num in mapped]


import unittest

class TestSolution(unittest.TestCase):
    def testSortJumbled(self):
        s = Solution()
        self.assertEqual(s.sortJumbled(mapping = [8,9,4,0,2,1,3,5,7,6], nums = [991,338,38]), 
                         [338,38,991])
        self.assertEqual(s.sortJumbled(mapping = [0,1,2,3,4,5,6,7,8,9], nums = [789,456,123]), 
                         [123,456,789])
        self.assertEqual(s.sortJumbled(mapping = [9,8,7,6,5,4,3,2,1,0], nums = [0,1,2,3,4,5,6,7,8,9]), 
                         [9,8,7,6,5,4,3,2,1,0])

if __name__ == '__main__':
    unittest.main()