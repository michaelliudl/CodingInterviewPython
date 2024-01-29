from typing import List

class Solution:

    def predictPartyVictory(self, senate: str) -> str:
        if not senate: return ''
        n=len(senate)
        banned=[0]*n
        while True:
            for i in range(n):
                if banned[i]:
                    continue
                s=senate[i]
                t='R' if s=='D' else 'D'
                tFound=False
                for j in range(i+1,n):
                    if not banned[j] and senate[j]==t:
                        banned[j]=1
                        tFound=True
                        break
                if not tFound:
                    for j in range(i-1):
                        if not banned[j] and senate[j]==t:
                            banned[j]=1
                            tFound=True
                            break
                if not tFound:
                    return 'Radiant' if s=='R' else 'Dire'


import unittest

class TestSolution(unittest.TestCase):
    def testPredictPartyVictory(self):
        s = Solution()
        self.assertEqual(s.predictPartyVictory(senate = "RD"), 'Radiant')
        self.assertEqual(s.predictPartyVictory(senate = "RDD"), 'Dire')
        self.assertEqual(s.predictPartyVictory(senate = "RRDDD"), 'Radiant')
        self.assertEqual(s.predictPartyVictory(senate = "RDDRD"), 'Dire')
        


if __name__ == '__main__':
    unittest.main()