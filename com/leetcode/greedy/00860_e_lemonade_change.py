from typing import List

class Solution:

    def lemonadeChange(self, bills: List[int]) -> bool:
        if not bills: return False
        d={}
        for b in bills:
            change=b-5
            while change>0:
                if change>=20 and 20 in d:
                    change-=20
                    d[20]-=1
                    if d[20]==0: del d[20]
                elif change>=10 and 10 in d:
                    change-=10
                    d[10]-=1
                    if d[10]==0: del d[10]
                elif change>=5 and 5 in d:
                    change-=5
                    d[5]-=1
                    if d[5]==0: del d[5]
                else:
                    break
            if change>0: return False
            if b in d:
                d[b]+=1
            else:
                d[b]=1
        return True



import unittest

class TestSolution(unittest.TestCase):
    def testLemonadeChange(self):
        s = Solution()
        self.assertEqual(s.lemonadeChange(bills = [5,5,5,10,20]), True)
        self.assertEqual(s.lemonadeChange(bills = [5,5,10,10,20]), False)
        


if __name__ == '__main__':
    unittest.main()