from typing import List,Deque

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        if not nums or k<=0: return 0
        map = {}
        ans,left,pairs = 0,0,0
        for i in range(len(nums)):
            cur = nums[i]
            if cur not in map:
                map[cur] = 0
            map[cur] += 1
            if map[cur] > 1:
                pairs += map[cur] - 1
            while pairs >= k:
                winOut = nums[left]
                goodElem = True if map[winOut] > 1 else False
                map[winOut] -= 1
                if goodElem:
                    pairs -= map[winOut]
                left += 1
            ans += left
        return ans



import unittest

class TestSolution(unittest.TestCase):
    def testCountGood(self):
        s = Solution()
        self.assertEqual(s.countGood(nums = [1,1,1,1,1], k = 10), 1)
        self.assertEqual(s.countGood(nums = [3,1,4,3,2,2,4], k = 2), 4)


if __name__ == '__main__':
    unittest.main()