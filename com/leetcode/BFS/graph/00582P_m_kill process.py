from typing import List,Deque

'''
You have n processes forming a rooted tree structure. You are given two integer arrays pid and ppid, where pid[i] is the ID of the ith process and ppid[i] is the ID of the ith process's parent process.

Each process has only one parent process but may have multiple children processes. Only one process has ppid[i] = 0, which means this process has no parent process (the root of the tree).

When a process is killed, all of its children processes will also be killed.

Given an integer kill representing the ID of a process you want to kill, return a list of the IDs of the processes that will be killed. You may return the answer in any order.
'''
class Solution:

    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:

        def buildGraph():
            for i in range(n):
                if ppid[i] not in graph:
                    graph[ppid[i]] = []
                graph[ppid[i]].append(pid[i])

        if not pid or not ppid or len(pid) != len(ppid) or kill < 0:
            return []
        n = len(pid)
        graph = {}
        buildGraph()
        result = []
        queue = Deque()
        queue.append(kill)
        while queue:
            cur = queue.popleft()
            result.append(cur)
            if cur in graph:
                for child in graph[cur]:
                    queue.append(child)
        return result

import unittest

class TestSolution(unittest.TestCase):
    def testWallsAndGates(self):
        s = Solution()
        rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
        s.wallsAndGates(rooms)
        self.assertEqual(rooms, [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]])
        rooms = [[-1]]
        s.wallsAndGates(rooms)
        self.assertEqual(rooms, [[-1]])
        


if __name__ == '__main__':
    unittest.main()