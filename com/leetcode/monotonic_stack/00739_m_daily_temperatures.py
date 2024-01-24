from typing import List
from typing import Deque


class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        r=[0]*len(temperatures)
        st=[0]
        for i in range(1,len(temperatures)):
            v=temperatures[i]
            while st and v>temperatures[st[-1]]:
                tIdx=st.pop()
                r[tIdx]=i-tIdx
            st.append(i)
        return r


import unittest

class TestSolution(unittest.TestCase):
    def testMaxSlidingWindow(self):
        s = Solution()
        self.assertEqual(s.maxSlidingWindowMonoToneQueue1([1,3,-1,-3,5,3,6,7],3), [3,3,5,5,6,7])
        self.assertEqual(s.maxSlidingWindowMonoToneQueue1([1],1), [1])



if __name__ == '__main__':
    unittest.main()