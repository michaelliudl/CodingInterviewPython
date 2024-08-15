from typing import List

class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(rem, startIndex, path: list):
            if rem == 0:
                res.append(path[:])
                return
            for i in range(startIndex, len(candidates)):
                # Skip remaining larger numbers
                if rem - candidates[i] < 0:
                    break
                # Skip duplicates which is used in previous rounds
                if i > startIndex and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(rem=(rem - candidates[i]), startIndex=(i + 1), path=path)
                path.pop()

        if not candidates:
            return []
        candidates.sort()
        res = []
        backtrack(rem=target, startIndex=0, path=[])
        return res
        

import unittest

class TestSolution(unittest.TestCase):
    def testCombinationSum2(self):
        s = Solution()
        self.assertEqual(s.combinationSum2([10,1,2,7,6,1,5], 8), [[1,1,6],[1,2,5],[1,7],[2,6]])
        self.assertEqual(s.combinationSum2([2,5,2,1,2], 5), [[1, 2, 2], [5]])
        


if __name__ == '__main__':
    unittest.main()