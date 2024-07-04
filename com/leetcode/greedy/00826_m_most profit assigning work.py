from typing import List

class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = list(zip(difficulty, profit))
        jobs.sort()
        worker.sort()
        i = j = 0
        maxProf = res = 0
        while i < len(jobs) and j < len(worker):
            if worker[j] >= jobs[i][0]:
                maxProf = max(maxProf, jobs[i][1])
                i += 1
            else:
                res += maxProf
                j += 1
        while j < len(worker):
            res += maxProf
            j += 1
        return res

    # Sort job's difficulty and profit pair, sort workers
    # For each worker, track max profit of jobs whose ability can do
    def maxProfitAssignment1(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        if not difficulty or not profit or not worker:
            return 0
        if len(difficulty) != len(profit):
            return 0
        n, m = len(difficulty), len(worker)
        jobs = [(difficulty[i], profit[i]) for i in range(n)]
        jobs.sort()
        worker.sort()
        result = 0
        maxProf = 0
        jobIndex = 0
        for w in worker:
            while jobIndex < n and w >= jobs[jobIndex][0]:
                maxProf = max(maxProf, jobs[jobIndex][1])
                jobIndex += 1
            result += maxProf
        return result


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