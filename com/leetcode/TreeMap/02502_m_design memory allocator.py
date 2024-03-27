from typing import List
from sortedcontainers import SortedList
import heapq

# Simulate since size is limited at 1000
class Allocator:

    def __init__(self, n: int):
        self.mem = [0] * n
        self.idToIndex = {}
    
    def allocate(self, size: int, mID: int) -> int:
        consecutiveFree = 0
        for i in range(len(self.mem)):
            if self.mem[i] == 0:
                consecutiveFree += 1
            else:
                consecutiveFree = 0
            if consecutiveFree == size:
                for j in range(i, i - size, -1):
                    self.mem[j] = mID
                    if mID not in self.idToIndex:
                        self.idToIndex[mID] = []
                    self.idToIndex[mID].append(j)
                return i - size + 1
        return -1
    
    def free(self, mID: int) -> int:
        if mID not in self.idToIndex:
            return 0
        for i in self.idToIndex[mID]:
            self.mem[i] = 0
        total = len(self.idToIndex[mID])
        del self.idToIndex[mID]
        return total

# Heap too slow
class Allocator1:

    def __init__(self, n: int):
        self.freeSpace = [[0, n]]
        self.allocated = {}

    def allocate(self, size: int, mID: int) -> int:
        temp = []
        while self.freeSpace and self.freeSpace[0][1] < size:
            temp.append(heapq.heappop(self.freeSpace))
        if not self.freeSpace:
            return -1
        start, freeSize = heapq.heappop(self.freeSpace)
        alloc = [start, size]
        if mID not in self.allocated:
            self.allocated[mID] = []
        heapq.heappush(self.allocated[mID], alloc)
        remFree = [start + size, freeSize - size]
        heapq.heappush(self.freeSpace, remFree)
        for i in range(len(temp) - 1, -1, -1):
            heapq.heappush(self.freeSpace, temp[i])
        return start

    def free(self, mID: int) -> int:
        if mID not in self.allocated:
            return 0
        total = 0
        for start, size in self.allocated[mID]:
            total += size
            heapq.heappush(self.freeSpace, [start, size])
        if len(self.freeSpace) > 1:
            temp = [heapq.heappop(self.freeSpace)]
            while self.freeSpace:
                prevStart, prevSize = temp[-1]
                curStart, curSize = heapq.heappop(self.freeSpace)
                if prevSize + prevSize == curStart:
                    temp.pop()
                    temp.append([prevStart, prevSize + curSize])
                else:
                    temp.append([curStart, curSize])
            for i in range(len(temp) - 1, -1, -1):
                heapq.heappush(self.freeSpace, temp[i])
        return total


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)

class Solution:
    pass
    
import unittest

class TestSolution(unittest.TestCase):
    def testAllocator(self):
        a = Allocator(10)
        self.assertEqual(a.allocate(size=1, mID=1), 0)
        self.assertEqual(a.allocate(size=1, mID=2), 1)
        self.assertEqual(a.allocate(size=1, mID=3), 2)
        self.assertEqual(a.free(mID=2), 1)
        self.assertEqual(a.allocate(size=3, mID=4), 3)
        self.assertEqual(a.allocate(size=1, mID=1), 1)
        self.assertEqual(a.allocate(size=1, mID=1), 6)
        self.assertEqual(a.free(mID=1), 3)
        self.assertEqual(a.allocate(size=10, mID=2), -1)
        self.assertEqual(a.free(mID=7), 0)

if __name__ == '__main__':
    unittest.main()