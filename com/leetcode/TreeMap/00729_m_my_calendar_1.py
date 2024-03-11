from typing import List

# TODO TreeMap

# Binary search
class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        if not self.bookings:
            self.bookings = [(start, end)]
            return True
        if end < self.bookings[0][0]:
            self.bookings.insert(0, (start, end))
            return True
        if start >= self.bookings[-1][1]:
            self.bookings.append((start, end))
            return True
        low, high = 0, len(self.bookings)
        while low < high:
            mid = low + (high - low) // 2
            midStart, midEnd = self.bookings[mid]
            if midStart < end and midEnd > start:
                return False
            elif midStart >= end:
                high = mid
            else:
                low = mid + 1
        self.bookings.insert(low, (start, end))
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