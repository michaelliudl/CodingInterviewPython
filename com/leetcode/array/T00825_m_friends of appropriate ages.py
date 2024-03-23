from typing import List

class Solution:

    # Sort and binary search
    def numFriendRequests(self, ages: List[int]) -> int:
        if not ages:
            return 0
        ages.sort()
        result = 0


    # O(n**2)
    def numFriendRequests1(self, ages: List[int]) -> int:

        def request(x, y):
            c1 = ages[y] <= 0.5 * ages[x] + 7
            c2 = ages[y] > ages[x]
            c3 = ages[y] > 100 and ages[x] < 100
            return not c1 and not c2 and not c3

        if not ages:
            return 0
        result = 0
        for i in range(len(ages) - 1):
            for j in range(i + 1, len(ages)):
                if request(i, j):
                    result += 1
                if request(j, i):
                    result += 1
        return result


import unittest

class TestSolution(unittest.TestCase):
    def testNumFriendRequests(self):
        s = Solution()
        self.assertEqual(s.numFriendRequests(ages = [16,16]), 2)
        self.assertEqual(s.numFriendRequests(ages = [16,17,18]), 2)
        self.assertEqual(s.numFriendRequests(ages = [20,30,100,110,120]), 3)

if __name__ == '__main__':
    unittest.main()