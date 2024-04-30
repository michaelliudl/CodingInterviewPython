from typing import List,Deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:

    # Topological sort with Kahn's algorithm
    # 1. Add all nodes with in-degree 0 to a queue.
    # 2. While the queue is not empty:
    #   2.1 Remove a node from the queue.
    #   2.2 For each outgoing edge from the removed node, decrement the in-degree of the destination node by 1.
    #   2.3 If the in-degree of a destination node becomes 0, add it to the queue.
    # 3. If the queue is empty and there are still nodes in the graph, the graph contains a cycle and cannot be topologically sorted.
    # 4. The nodes in the queue represent the topological ordering of the graph.
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            inDegree[course] += 1       # Increment in-degree of course per each of its prerequisites
        queue = Deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
        res = []
        while queue:
            course = queue.popleft()    # `course` with prerequisites or all prerequisites already taken
            res.append(course)
            for neighbor in graph[course]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
        return res if len(res) == numCourses else []    # There is cycle if we can't reduce all courses in-degree to 0

    # DFS with states: 0 = Init, 1 = Visiting, 2 = Visited
    def findOrderDFS(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        def dfs(course):
            if states[course] == 1:     # `course` is in seen again while dfs from another one
                return True
            if states[course] == 2:
                return False
            states[course] = 1
            for neighbor in graph[course]:
                if dfs(neighbor):
                    return True
            states[course] = 2
            res.append(course)
            return False

        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)
        states = [0] * numCourses
        res = []
        for i in range(numCourses):
            if dfs(i):          # Any course has cycle
                return []
        res.reverse()           # We added course to result before its prerequites
        return res

    # BFS and collect courses without prerequisites and remove them from the graph
    def findOrderBFS(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
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