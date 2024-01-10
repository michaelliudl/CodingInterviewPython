from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if nums is None:
            return
        s,m,e = 0,0,len(nums)-1
        while m<=e:
            if nums[m]==0:
                nums[s],nums[m]=nums[m],nums[s]
                s+=1
                m+=1
            elif nums[m]==1:
                m+=1
            else:
                nums[m],nums[e]=nums[e],nums[m]
                e-=1
        return

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def testSortColors(self):
        input = [2,0,2,1,1,0]
        expected = [0,0,1,1,2,2]
        self.s.sortColors(input)
        self.assertEqual(input, expected)

if __name__ == '__main__':
    unittest.main()