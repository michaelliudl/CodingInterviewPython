from typing import Deque

class Logger:

    def __init__(self):
        self.logMap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        result = (message not in self.logMap) or (timestamp >= self.logMap[message] + 10)
        if result:
            self.logMap[message] = timestamp
        return result
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

class Solution:
    pass
    
import unittest

class TestSolution(unittest.TestCase):
    def testLogger(self):
        log = Logger()
        self.assertEqual(log.shouldPrintMessage(1, 'foo'), True)
        self.assertEqual(log.shouldPrintMessage(2, 'bar'), True)
        self.assertEqual(log.shouldPrintMessage(3, 'foo'), False)
        self.assertEqual(log.shouldPrintMessage(8, 'bar'), False)
        self.assertEqual(log.shouldPrintMessage(10, 'foo'), False)
        self.assertEqual(log.shouldPrintMessage(11, 'foo'), True)


if __name__ == '__main__':
    unittest.main()
