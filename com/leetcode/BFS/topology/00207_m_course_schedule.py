from typing import List,Deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:

    # Use DFS and visit status to detect cycle
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def cache():
            for pair in prerequisites:
                course,pre=pair[0],pair[1]
                if course in d:
                    d[course].append(pre)
                else:
                    d[course]=[pre]

        def dfs(course):
            if visited[course]==1:      # Found current course again
                return False
            visited[course]=1
            if course in d:
                for pre in d[course]:
                    if visited[pre]!=2:
                        if not dfs(pre):
                            return False
            visited[course]=2
            return True

        if not prerequisites: return True
        d={}
        cache()
        visited=[0]*numCourses          # States: 0, not visited; 1, current; 2, visisted
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

    # Almost time out
    def canFinishBFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if not prerequisites: return True
        d={}
        for pair in prerequisites:
            course,pre=pair[0],pair[1]
            if course in d:
                d[course].append(pre)
            else:
                d[course]=[pre]
        for course in d.keys():
            visited={}
            q=Deque()
            for pre in d[course]:
                q.append(pre)
            while q:
                cur=q.popleft()
                if cur==course:
                    return False
                visited[cur]=1
                if cur in d:
                    for pre in d[cur]:
                        if not pre in visited:
                            q.append(pre)
        return True
        

import unittest

class TestSolution(unittest.TestCase):
    def testCanFinish(self):
        s = Solution()
        self.assertEqual(s.canFinish(numCourses = 2, prerequisites = [[1,0]]), True)
        self.assertEqual(s.canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]), False)
        


if __name__ == '__main__':
    unittest.main()