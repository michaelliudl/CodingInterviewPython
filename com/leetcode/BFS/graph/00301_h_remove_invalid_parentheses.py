from typing import List, Deque

class Solution:

    # This is a graph problem that start string is the start node. Deleting one ( or ) forms an edge.
    # Results of one deletion are level 1 nodes, and so on.
    # BFS this graph and check for valid nodes on lowest level which are valid results of minimum deletion.
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        # Validate parenthesis without stack
        def isValid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        if not s:
            return []
        if isValid(s):
            return [s]
        result = set()
        used = set()            # Deduplicate
        queue = Deque()
        queue.append(s)
        while queue:
            curLen = len(queue)
            for _ in range(curLen):
                cur = queue.popleft()
                if isValid(cur):
                    result.add(cur)
                else:
                    for i in range(len(cur)):
                        if cur[i] in ('(', ')'):
                            nextString = cur[:i] + cur[(i + 1):]
                            if nextString not in used:
                                queue.append(nextString)
                                used.add(nextString)
            if result:
                break
        return list(result)

import unittest

class TestSolution(unittest.TestCase):
    def testRemoveInvalidParentheses(self):
        s = Solution()
        self.assertEqual(s.removeInvalidParentheses(s = "()((((((()l("), ["()()l"])
        self.assertEqual(set(s.removeInvalidParentheses(s = "()())()")), set(["(())()","()()()"]))
        self.assertEqual(set(s.removeInvalidParentheses(s = "(a)())()")), set(["(a())()","(a)()()"]))
        self.assertEqual(s.removeInvalidParentheses(s = ")("), [""])


if __name__ == '__main__':
    unittest.main()