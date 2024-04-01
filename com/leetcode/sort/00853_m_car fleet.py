from typing import List
from typing import Deque


class Solution:

    # Calculate each car's time to reach target
    # Sort by position and count each strictly increasing time
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if target <= 0 or not position or not speed or len(position) != len(speed):
            return 0
        n = len(position)
        posAndTimeToTarget = [None] * n
        for i in range(n):
            time = (target - position[i]) / speed[i]
            posAndTimeToTarget[i] = (position[i], time)
        posAndTimeToTarget.sort()
        maxTime = 0
        result = 0
        for i in range(len(posAndTimeToTarget) - 1, -1, -1):
            _, time = posAndTimeToTarget[i]
            if time > maxTime:
                maxTime = time
                result += 1
        return result

import unittest

class TestSolution(unittest.TestCase):
    def testCarFleet(self):
        s = Solution()
        self.assertEqual(s.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]), 3)
        self.assertEqual(s.carFleet(target = 10, position = [3], speed = [3]), 1)
        self.assertEqual(s.carFleet(target = 100, position = [0,2,4], speed = [4,2,1]), 1)



if __name__ == '__main__':
    unittest.main()