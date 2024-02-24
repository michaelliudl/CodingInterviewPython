from typing import List
import heapq

# Map and stack, O(n)
class FreqStack:

    def __init__(self):
        self.valFreqMap = {}    # Map from value to its frequency
        self.freqValMap = {}    # Map from frequency to list of values in order of pushing
        self.maxFreq = 0

    def push(self, val: int) -> None:
        if val not in self.valFreqMap:
            self.valFreqMap[val] = 0
        self.valFreqMap[val] += 1
        freq = self.valFreqMap[val]
        if freq not in self.freqValMap:
            self.freqValMap[freq] = []
        self.freqValMap[freq].append(val)
        self.maxFreq = max(self.maxFreq, freq)

    def pop(self) -> int:
        if self.maxFreq == 0:
            return -1
        val = self.freqValMap[self.maxFreq].pop()
        self.valFreqMap[val] -= 1
        if not self.freqValMap[self.maxFreq]:
            self.maxFreq -= 1
        return val

# Use heap, O(nlogn)
class FreqStack1:

    def __init__(self):
        self.stack = []
        self.map = {}
        self.heap = []

    def push(self, val: int) -> None:
        index = len(self.stack)
        self.stack.append(val)
        if val not in self.map:
            self.map[val] = []
        self.map[val].append(-index)
        exists = False
        for elem in self.heap:
            if elem[2] == val:
                exists = True
                elem[0] -= 1
                elem[1] = -index
                heapq.heapify(self.heap)
                break
        if not exists:
            heapq.heappush(self.heap, [-1, -index, val])

    def pop(self) -> int:
        freq,lastIndex,val = heapq.heappop(self.heap)
        freq += 1
        self.stack[lastIndex] = -1
        self.map[val].pop()
        if not self.map[val]:
            del self.map[val]
        if freq < 0:
            heapq.heappush(self.heap, [freq, self.map[val][-1], val])
        return val



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

class Solution:
    pass


import unittest

class TestSolution(unittest.TestCase):

    def testFreqStack(self):
        fs = FreqStack()
        fs.push(4)
        fs.push(0)
        fs.push(9)
        fs.push(3)
        fs.push(4)
        fs.push(2)
        self.assertEqual(fs.pop(), 4)
        fs.push(6)
        self.assertEqual(fs.pop(), 6)
        fs.push(1)
        self.assertEqual(fs.pop(), 1)
        fs.push(1)
        self.assertEqual(fs.pop(), 1)
        fs.push(4)
        self.assertEqual(fs.pop(), 4)
        self.assertEqual(fs.pop(), 2)
        self.assertEqual(fs.pop(), 3)
        self.assertEqual(fs.pop(), 9)
        self.assertEqual(fs.pop(), 0)
        self.assertEqual(fs.pop(), 4)

    def testFreqStack2(self):
        fs = FreqStack()
        fs.push(1)
        fs.push(0)
        fs.push(0)
        fs.push(1)
        fs.push(5)
        fs.push(4)
        fs.push(1)
        fs.push(5)
        fs.push(1)
        fs.push(6)
        self.assertEqual(fs.pop(), 1)
        self.assertEqual(fs.pop(), 1)
        self.assertEqual(fs.pop(), 5)
        self.assertEqual(fs.pop(), 1)
        self.assertEqual(fs.pop(), 0)

    def testFreqStack1(self):
        fs = FreqStack()
        fs.push(5)
        fs.push(7)
        fs.push(5)
        fs.push(7)
        fs.push(4)
        fs.push(5)
        self.assertEqual(fs.pop(), 5)
        self.assertEqual(fs.pop(), 7)
        self.assertEqual(fs.pop(), 5)
        self.assertEqual(fs.pop(), 4)



if __name__ == '__main__':
    unittest.main()