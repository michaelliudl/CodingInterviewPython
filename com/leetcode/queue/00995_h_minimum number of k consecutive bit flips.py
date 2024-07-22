from typing import List,Deque

class Solution:

    # Greedily flip each `k` elements group if the first element in the group is 0
    # Use queue to track the flipped index in the previous `k` index
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        queue = Deque()
        res = 0
        for i, num in enumerate(nums):
            while queue and i > (queue[0] + k - 1):     # Earlier flipped index is out of `k` size window
                queue.popleft()
            # Length of `queue` is number of previous flips that affected current index `i`
            if (num + len(queue)) % 2 == 0:     # This results in actual number at `i` after previous flips
                if i + k > n:       # Not enough to flip after this `0`
                    return -1
                res += 1
                queue.append(i)
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testMinKBitFlips(self):
        s = Solution()
        self.assertEqual(s.minKBitFlips(nums = [0,1,0], k = 1), 2)
        self.assertEqual(s.minKBitFlips(nums = [1,1,0], k = 2), -1)
        self.assertEqual(s.minKBitFlips(nums = [0,0,0,1,0,1,1,0], k = 3), 3)

if __name__ == '__main__':
    unittest.main()