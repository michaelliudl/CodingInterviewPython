from typing import List

class Solution:

    def judgeCircle(self, moves: str) -> bool:
        if not moves: return True
        dirs={'U': (-1,0), 'D': (1,0), 'L': (0,-1), 'R': (0,1)}
        pos=(0,0)
        for m in moves:
            pos=((pos[0]+dirs[m][0], pos[1]+dirs[m][1]))
        return pos==(0,0)

import unittest

class TestSolution(unittest.TestCase):
    def testbulbSwitch(self):
        s = Solution()
        self.assertEqual(s.bulbSwitch(3), 1)
        self.assertEqual(s.bulbSwitch(0), 0)
        self.assertEqual(s.bulbSwitch(1), 1)


if __name__ == '__main__':
    unittest.main()