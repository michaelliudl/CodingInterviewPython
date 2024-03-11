from typing import List,Deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:

    # Union Find

    # BFS
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        def buildGraph():
            for a, b in prerequisites:
                if a not in graph:
                    graph[a] = set()
                graph[a].add(b)
            for i in range(numCourses):
                if i not in graph:
                    graph[i] = set()

        if not prerequisites:
            return [i for i in range(numCourses)]
        graph = {}
        buildGraph()
        ans = []
        taken = set()
        while graph:
            newCourse = []
            for c, pres in graph.items():
                presTaken = set()
                for pre in pres:
                    if pre in taken:
                        presTaken.add(pre)
                for p in presTaken:
                    pres.remove(p)
                if not pres:
                    ans.append(c)
                    taken.add(c)
                    newCourse.append(c)
            if not newCourse:
                break
            for c in newCourse:
                del graph[c]
        return ans if len(ans) == numCourses else []

import unittest

class TestSolution(unittest.TestCase):
    def testFindOrder(self):
        s = Solution()
        self.assertEqual(s.findOrder(numCourses = 2, prerequisites = [[1,0]]), [0,1])
        self.assertEqual(s.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]), [0,1,2,3])
        self.assertEqual(s.findOrder(numCourses = 1, prerequisites = []), [0])


if __name__ == '__main__':
    unittest.main()