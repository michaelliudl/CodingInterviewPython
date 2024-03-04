from typing import List,Optional

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        if not s:
            return s
        freqs = {}
        for ch in s:
            freqs[ch] = freqs.get(ch, 0) + 1
        ans = []
        for ch in order:
            if ch in freqs:
                for _ in range(freqs[ch]):
                    ans.append(ch)
                del freqs[ch]
        for ch, freq in freqs.items():
            for _ in range(freq):
                ans.append(ch)
        return ''.join(ans)

import unittest

class TestSolution(unittest.TestCase):
    def testHasCycle(self):
        s = Solution()
        self.assertEqual(s.hasCycle(ListNode(1,ListNode(2,None))), False)


if __name__ == '__main__':
    unittest.main()