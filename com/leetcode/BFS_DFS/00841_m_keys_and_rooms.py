from typing import List,Deque

class Solution:
    
    def canVisitAllRoomsBFS(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return False
        n=len(rooms)
        status=[0]*n
        status[0]=1
        q=Deque()
        for k in rooms[0]:
            q.append(k)
        while q:
            key=q.popleft()
            status[key]=1
            for k in rooms[key]:
                if not status[k]:
                    q.append(k)
        return sum(status)==n

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        def dfs(roomNo, status):
            status[roomNo]=1
            for key in rooms[roomNo]:
                if not status[key]:
                    dfs(key, status)
        
        if not rooms:
            return False
        n=len(rooms)
        status=[0]*n
        dfs(0, status)
        return sum(status)==n





        

import unittest

class TestSolution(unittest.TestCase):
    def testCanVisitAllRooms(self):
        s = Solution()
        self.assertEqual(s.canVisitAllRooms(rooms = [[1],[2],[3],[]]), True)
        self.assertEqual(s.canVisitAllRooms(rooms = [[1,3],[3,0,1],[2],[0]]), False)
        


if __name__ == '__main__':
    unittest.main()