from typing import List

class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(candidates, rem, startIndex, r:list, path: list):
            if rem==0:
                r.append(path[:])
                return
            for i in range(startIndex, len(candidates)):
                # Skip remaining larger numbers
                if rem-candidates[i]<0:
                    break
                # Skip duplicates which is used in previous rounds
                if i>startIndex and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(candidates, rem=rem-candidates[i], startIndex=i+1, r=r, path=path)
                path.pop()

        if not candidates:
            return []
        candidates=sorted(candidates)
        r=[]
        backtrack(candidates, target, startIndex=0, r=r, path=[])
        return r
        

import unittest

class TestSolution(unittest.TestCase):
    def testCombinationSum2(self):
        s = Solution()
        self.assertEqual(s.combinationSum2([10,1,2,7,6,1,5], 8), [[1,1,6],[1,2,5],[1,7],[2,6]])
        self.assertEqual(s.combinationSum2([2,5,2,1,2], 5), [[5],[2,1,2]])
        


if __name__ == '__main__':
    unittest.main()