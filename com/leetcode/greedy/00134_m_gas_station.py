from typing import List

class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if not gas or not cost or len(gas)!=len(cost):
            return -1
        n=len(gas)
        resAll,minRes=0,float('inf')
        for i in range(n):
            res = gas[i]-cost[i]
            resAll+=res
            minRes=min(minRes,resAll)
        
        if resAll<0: return -1
        if minRes>=0: return 0

        for i in range(n-1,-1,-1):
            res = gas[i]-cost[i]
            minRes+=res
            if minRes>=0: return i
        return -1


    # Time out
    def canCompleteCircuitBrute(self, gas: List[int], cost: List[int]) -> int:
        if not gas or not cost or len(gas)!=len(cost):
            return -1
        n=len(gas)
        for i in range(n):
            res=gas[i]-cost[i]
            if res<0: continue
            next=(i+1)%n
            while res>0 and next!=i:
                res += gas[next]-cost[next]
                next = (next+1)%n
            if res>=0 and next==i: return i
        return -1



import unittest

class TestSolution(unittest.TestCase):
    def testCanCompleteCircuit(self):
        s = Solution()
        self.assertEqual(s.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]), 3)
        self.assertEqual(s.canCompleteCircuit(gas = [2,3,4], cost = [3,4,3]), -1)
        


if __name__ == '__main__':
    unittest.main()