from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    # def __eq__(self, __value: object) -> bool:
    #     return isinstance(__value, ListNode) and self.val == __value.val and self.next == __value.next

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        if n == 0 or not logs:
            return []
        ans = [0] * n
        stack = []
        prevTime = 0            # Track previous `log` time
        for log in logs:
            funcStr, tag, timeStr = log.split(':')
            func, time = int(funcStr), int(timeStr)
            if tag == 'start':
                if stack:
                    funcTopStr, _, _ = stack[-1]
                    funcTop = int(funcTopStr)
                    ans[funcTop] += (time - prevTime)       # Time diff for `start` log
                stack.append((func, tag, time))
                prevTime = time                             # Update prev time for `start`
            else:
                if not stack:
                    return []
                funcTopStr, tagTop, _ = stack.pop()
                funcTop = int(funcTopStr)
                if funcTop != func or tagTop != 'start':
                    return []
                ans[func] += (time - prevTime + 1)          # Time diff for `end` tag needs to +1
                prevTime = time + 1                         # Update prev time for `end` with time +1
        return ans





import unittest

class TestSolution(unittest.TestCase):
    def testExclusiveTime(self):
        s = Solution()
        self.assertEqual(s.exclusiveTime(n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]), [3,4])
        self.assertEqual(s.exclusiveTime(n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]), [8])
        self.assertEqual(s.exclusiveTime(n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]), [7,1])


if __name__ == '__main__':
    unittest.main()