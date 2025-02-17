from typing import List

class Solution:

    # Use +1/-1 to counter number of forward/backward shifts
    # Use start to indicate shifting range, and end+1 to indicate out of range
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        shiftRecords = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            diff = 1 if direction == 1 else -1
            shiftRecords[start] += diff
            shiftRecords[end + 1] -= diff
        curShift = 0
        res = []
        for i, char in enumerate(s):
            curShift = (curShift + shiftRecords[i]) % 26
            shifted = (ord(char) - ord('a') + curShift + 26) % 26
            res.append(chr(shifted + ord('a')))
        return ''.join(res)

        

import unittest

class TestSolution(unittest.TestCase):

    def testInsert(self):
        s=Solution()
        self.assertEqual(s.insert(intervals = [], newInterval = [5,7]), [[5,7]])
        self.assertEqual(s.insert(intervals = [[1,3],[6,9]], newInterval = [2,5]), [[1,5],[6,9]])
        self.assertEqual(s.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]), [[1,2],[3,10],[12,16]])

if __name__ == '__main__':
    unittest.main()