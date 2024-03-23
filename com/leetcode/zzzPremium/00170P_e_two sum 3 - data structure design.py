from typing import List

class TwoSum:

    def __init__(self):
        self.numMap = {}
        self.seq = 0

    def add(self, number: int) -> None:
        if number not in self.numMap:
            self.numMap[number] = set()
        self.numMap[number].add(self.seq)
        self.seq += 1

    def find(self, value: int) -> bool:
        for num, seqs in self.numMap.items():
            diff = value - num
            if diff == num and len(seqs) > 1:
                return True
            if diff != num and diff in self.numMap:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

class Solution:
    pass
    
import unittest

class TestSolution(unittest.TestCase):
    def testTwoSum(self):
        ts = TwoSum()
        ts.add(1)
        ts.add(3)
        ts.add(5)
        self.assertEqual(ts.find(4), True)
        self.assertEqual(ts.find(7), False)
    
    def testTwoSum1(self):
        ts = TwoSum()
        ts.add(3)
        ts.add(1)
        ts.add(2)
        self.assertEqual(ts.find(3), True)
    
    def testTwoSum2(self):
        ts = TwoSum()
        ts.add(0)
        ts.add(-1)
        ts.add(1)
        self.assertEqual(ts.find(0), True)


if __name__ == '__main__':
    unittest.main()
