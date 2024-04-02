from typing import List

'''
Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest time slot that works for both of them and is of duration duration.

If there is no common time slot that satisfies the requirements, return an empty array.

The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.

It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.
'''

class Solution:

    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        if not slots1 or not slots2:
            return []
        slots1.sort()
        slots2.sort()
        i = j = 0
        while i < len(slots1) and j < len(slots2):
            if slots1[i][1] <= slots2[j][0]:
                i += 1
            elif slots2[j][1] <= slots1[i][0]:
                j += 1
            elif slots1[i][1] > slots2[j][0] or slots2[j][1] > slots1[i][0]:
                minEnd = min(slots1[i][1], slots2[j][1])
                maxStart = max(slots1[i][0], slots2[j][0])
                inter = minEnd - maxStart
                if inter >= duration:
                    return [maxStart, maxStart + duration]
                elif slots1[i][1] <= slots2[j][1]:
                    i += 1
                elif slots2[j][1] <= slots1[i][1]:
                    j += 1
        return []



import unittest

class TestSolution(unittest.TestCase):
    def testMinAvailableDuration(self):
        s = Solution()
        self.assertEqual(s.minAvailableDuration(slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8), [60,68])
        self.assertEqual(s.minAvailableDuration(slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12), [])
        


if __name__ == '__main__':
    unittest.main()