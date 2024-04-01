from typing import List,Deque

# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        if not employees:
            return 0
        graph = {employee.id: (employee.importance, employee.subordinates) for employee in employees}
        if id not in graph:
            return 0
        result = 0
        queue = Deque()
        queue.append(id)
        while queue:
            curId = queue.popleft()
            if curId in graph:
                value, subs = graph[curId]
                result += value
                for sub in subs:
                    queue.append(sub)
        return result



        

import unittest

class TestSolution(unittest.TestCase):
    def testNumEnclaves(self):
        s = Solution()
        self.assertEqual(s.numEnclaves(grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]), 3)
        self.assertEqual(s.numEnclaves(grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]), 0)
        


if __name__ == '__main__':
    unittest.main()