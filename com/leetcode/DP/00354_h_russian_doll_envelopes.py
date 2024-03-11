from typing import List

class Solution:

    # Sort by width asc and height desc
    # Use LIS (#300) algo on height. DP and binary search
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort(key = lambda env: (env[0], -env[1]))
        # Do LIS algo on height
        dp = []
        for _, height in envelopes:
            low, high = 0, len(dp)
            while low < high:
                mid = low + (high - low) // 2
                if dp[mid] < height:        # Height sorted desc
                    low = mid + 1
                else:
                    high = mid
            if high == len(dp):
                dp.append(height)
            else:
                dp[high] = height
        return len(dp)

    # Sort and DP
    # dp[i] = max(dp[i], dp[j] + 1), j loops backwards from i and envelope j is smaller than envelope i
    # Sequential search timeout.
    def maxEnvelopesSequentialDP(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort()
        n = len(envelopes)
        dp = [1] * n
        for i in range(1, n):
            wI, hI = envelopes[i]
            for j in range(i - 1, -1, -1):
                wJ, hJ = envelopes[j]
                if wI > wJ and hI > hJ:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    # Sort and greedy, wrong answer on case # 3
    def maxEnvelopesWrong(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort()
        ans = 1
        prevW, prevH = envelopes[0]
        for i in range(1, len(envelopes)):
            curW, curH = envelopes[i]
            if curW > prevW and curH > prevH:
                ans += 1
                prevW, prevH = curW, curH
        return ans


import unittest

class TestSolution(unittest.TestCase):
    def testMaxEnvelopes(self):
        s = Solution()
        self.assertEqual(s.maxEnvelopes(envelopes = [[5,4],[6,4],[6,7],[2,3]]), 3)
        self.assertEqual(s.maxEnvelopes(envelopes = [[1,1],[1,1],[1,1]]), 1)
        self.assertEqual(s.maxEnvelopes(envelopes = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]), 5)
        self.assertEqual(s.maxEnvelopes(envelopes = [[46,89],[50,53],[52,68],[72,45],[77,81]]), 3)


if __name__ == '__main__':
    unittest.main()