from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        first, second, firstLen, secondLen = 0, 0 , len(firstList), len(secondList)
        ans = []
        while first < firstLen and second < secondLen:
            firstStart, firstEnd = firstList[first]
            secondStart, secondEnd = secondList[second]
            if firstEnd < secondStart:
                first += 1
                continue
            if secondEnd < firstStart:
                second += 1
                continue
            ans.append([max(firstStart, secondStart), min(firstEnd, secondEnd)])
            if firstEnd == secondEnd:
                first += 1
                second += 1
            elif firstEnd < secondEnd:
                first += 1
            else:
                second += 1
        return ans




import unittest

class TestSolution(unittest.TestCase):
    def testIntervalIntersection(self):
        s = Solution()
        self.assertEqual(s.intervalIntersection(firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]), 
                         [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]])
        self.assertEqual(s.intervalIntersection(firstList = [[1,3],[5,9]], secondList = []), [])



if __name__ == '__main__':
    unittest.main()