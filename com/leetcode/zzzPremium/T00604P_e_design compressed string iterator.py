from typing import List

class StringIterator:

    def __init__(self, compressedString: str):
        self.chars = []
        self.indices = []
        self.total = 0
        self.cur = 0

        def addIndex(numStart, i):
            if numStart >= 0:
                count = int(compressedString[numStart:i])
                if self.indices:
                    count += self.indices[-1]
                self.total = count
                self.indices.append(count)

        numStart = -1
        for i in range(len(compressedString)):
            if '0' <= compressedString[i] <= '9':
                if numStart < 0:
                    numStart = i
            else:
                self.chars.append(compressedString[i])
                addIndex(numStart, i)
                numStart = -1
        addIndex(numStart, len(compressedString))

    def next(self) -> str:

        def search():
            low, high = 0, len(self.indices)
            while low < high:
                mid = low + (high - low) // 2
                if self.cur == self.indices[mid]:
                    return mid
                elif self.cur < self.indices[mid]:
                    high = mid
                else:
                    low = mid + 1
            return low

        if self.hasNext():
            charIndex = search()
            self.cur += 1
            return self.chars[charIndex]
        return ' '

    def hasNext(self) -> bool:
        return self.cur < self.total


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()

class Solution:
    pass
    
import unittest

class TestSolution(unittest.TestCase):
    def testStringIterator(self):
        s = StringIterator("L1e2t1C1o1d1e1")
        self.assertEqual(s.next(), 'L')
        self.assertEqual(s.next(), 'e')
        self.assertEqual(s.next(), 'e')
        self.assertEqual(s.next(), 't')
        self.assertEqual(s.next(), 'C')
        self.assertEqual(s.next(), 'o')
        self.assertEqual(s.hasNext(), True)
        self.assertEqual(s.next(), 'd')
        self.assertEqual(s.hasNext(), True)


if __name__ == '__main__':
    unittest.main()
