from typing import List,Deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        def buildGraph():
            for pre, course in prerequisites:
                if pre not in graph:
                    graph[pre] = set()
                graph[pre].add(course)

        def bfs(start, end):
            queue = Deque()
            queue.append(start)
            visited = set()
            visited.add(start)
            while queue:
                course = queue.popleft()
                if course == end:
                    return True
                if course in graph:
                    for neighbor in graph[course]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
            return False

        if not prerequisites:
            return [False] * len(queries)
        graph = {}
        buildGraph()
        ans = [False] * len(queries)
        for i, [courseU, courseV] in enumerate(queries):
            if courseU in graph:
                ans[i] = bfs(start=courseU, end=courseV)
        return ans

import unittest

class TestSolution(unittest.TestCase):
    def testCheckIfPrerequisite(self):
        s = Solution()
        self.assertEqual(s.checkIfPrerequisite(numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]), [False, True])
        self.assertEqual(s.checkIfPrerequisite(numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]), [False, False])
        self.assertEqual(s.checkIfPrerequisite(numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]), [True, True])


if __name__ == '__main__':
    unittest.main()