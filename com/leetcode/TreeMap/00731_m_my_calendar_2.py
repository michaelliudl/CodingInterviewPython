from typing import List

# TODO TreeMap

# Brute by keeping overlapping and non-overlapping intervals,
# O(n**2)
class MyCalendarTwo:

    def __init__(self):
        self.overlaps = []
        self.nonOverlaps = []

    def book(self, start: int, end: int) -> bool:
        # Check against existing overlapping
        for olStart, olEnd in self.overlaps:
            if start < olEnd and end > olStart: # alternatively `not (end <= olStart or start >= olEnd)`
                return False
        for nonOlStart, nonOlEnd in self.nonOverlaps:
            if start < nonOlEnd and end > nonOlStart:
                self.overlaps.append((max(nonOlStart, start), min(nonOlEnd, end)))    # Track overlapping portion of the intervals
        self.nonOverlaps.append((start, end))
        return True



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

class Solution:
    pass


import unittest

class TestSolution(unittest.TestCase):
    def testMyCalendar(self):
        mc = MyCalendar()
        self.assertEqual(mc.book(10, 20), True)
        self.assertEqual(mc.book(15, 25), False)
        self.assertEqual(mc.book(20, 30), True)


if __name__ == '__main__':
    unittest.main()