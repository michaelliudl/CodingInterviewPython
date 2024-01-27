from typing import List

class Solution:

    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums)<=1: return 0
        steps,n=0,len(nums)
        cur,next=0,0
        for i in range(n):
            next = max(next, i+nums[i])
            if i==cur:
                cur=next
                steps+=1
                if next>=(n-1):
                    break
        return steps



import unittest

class TestSolution(unittest.TestCase):
    def testJump(self):
        s = Solution()
        self.assertEqual(s.jump(nums = [2,3,1,1,4]), 2)
        self.assertEqual(s.jump(nums = [2,3,0,1,4]), 2)
        self.assertEqual(s.jump(nums = [5,9,3,2,1,0,2,3,3,1,0,0]), 3)
        


if __name__ == '__main__':
    unittest.main()