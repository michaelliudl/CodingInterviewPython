import random
from typing import List

class Solution:

    def minSteps(self, s: str, t: str) -> int:
        if not s:
            return len(t)
        if not t:
            return len(s)
        countS = {}
        for char in s:
            countS[char] = countS.get(char, 0) + 1
        countT = {}
        for char in t:
            countT[char] = countT.get(char, 0) + 1
        uniqs = set(list(s))
        for char in t:
            uniqs.add(char)
        result = 0
        for char in uniqs:
            charS = countS[char] if char in countS else 0
            charT = countT[char] if char in countT else 0
            result += abs(charS - charT)
        return result // 2

import unittest

class TestSolution(unittest.TestCase):

    def testRandomizedSet(self):
        rs = RandomizedSet()
        self.assertEqual(rs.remove(0), False)
        self.assertEqual(rs.remove(0), False)
        self.assertEqual(rs.insert(0), True)
        self.assertIn(rs.getRandom(), (0,1))
        self.assertEqual(rs.remove(0), True)
        self.assertEqual(rs.insert(0), True)

    def testRandomizedSet1(self):
        rs = RandomizedSet()
        self.assertEqual(rs.insert(1), True)
        self.assertEqual(rs.remove(2), False)
        self.assertEqual(rs.insert(2), True)
        self.assertIn(rs.getRandom(), (1,2))
        self.assertEqual(rs.remove(1), True)
        self.assertEqual(rs.insert(2), False)
        self.assertIn(rs.getRandom(), (1,2))


if __name__ == '__main__':
    unittest.main()