from typing import List, DefaultDict

class Solution:

    def lemonadeChange(self, bills: List[int]) -> bool:
        billMap = DefaultDict(int)
        for bill in bills:
            change = bill-5
            while change > 0:
                if change >= 20 and billMap[20] > 0:
                    change -= 20
                    billMap[20] -= 1
                elif change >= 10 and billMap[10] > 0:
                    change -= 10
                    billMap[10] -= 1
                elif change >= 5 and billMap[5] > 0:
                    change -= 5
                    billMap[5] -= 1
                else:
                    break
            if change > 0: 
                return False
            billMap[bill] += 1
        return True



import unittest

class TestSolution(unittest.TestCase):
    def testLemonadeChange(self):
        s = Solution()
        self.assertEqual(s.lemonadeChange(bills = [5,5,5,10,20]), True)
        self.assertEqual(s.lemonadeChange(bills = [5,5,10,10,20]), False)
        


if __name__ == '__main__':
    unittest.main()