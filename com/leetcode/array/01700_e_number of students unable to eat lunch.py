from typing import List,Deque

class Solution:

    # Simulate with queue
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        qStu = Deque(students)
        qSand = Deque(sandwiches)
        while True:
            pick = False
            curLen = len(qStu)
            for _ in range(curLen):
                if qStu[0] == qSand[0]:
                    pick = True
                    qStu.popleft()
                    qSand.popleft()
                else:
                    qStu.append(qStu.popleft())
            if not pick:
                break
        return len(qStu)

import unittest

class TestSolution(unittest.TestCase):

    def testPivotIndex(self):
        s=Solution()
        self.assertEqual(s.pivotIndex(nums = [1,7,3,6,5,6]), 3)
        self.assertEqual(s.pivotIndex(nums = [2,1,-1]), 0)
        self.assertEqual(s.pivotIndex(nums = [1,2,3]), -1)

if __name__ == '__main__':
    unittest.main()