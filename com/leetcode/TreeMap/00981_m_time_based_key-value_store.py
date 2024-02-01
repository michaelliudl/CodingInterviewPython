from typing import List

class TimeMapLinear:

    def __init__(self):
        self.map={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.map:
            self.map[key]=[]
        self.map[key].append((timestamp, value))    # Timestamp no need to sort

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.map:
            return ''
        for i in range(len(self.map[key])-1,-1,-1):     # Linear search is also AC
            if self.map[key][i][0]<=timestamp:
                return self.map[key][i][1]
        return ''
class TimeMap:

    def __init__(self):
        self.map={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.map:
            self.map[key]=[]
        self.map[key].append((timestamp, value))    # timestamp should be monotonic increasing

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.map:
            return ''
        values=self.map[key]
        low,high=0,len(values)
        while low<high:
            mid=low+(high-low)//2
            if values[mid][0]>timestamp:
                high=mid
            else:
                low=mid+1
        return values[low-1][1] if low>0 else ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

class Solution:
    pass


import unittest

class TestSolution(unittest.TestCase):
    def testTimeMap(self):
        tm=TimeMap()
        tm.set('foo','bar',1)
        v=tm.get('foo',1)
        self.assertEqual(v,'bar')
        v=tm.get('foo',3)
        self.assertEqual(v,'bar')
        tm.set('foo','bar2',4)
        v=tm.get('foo',4)
        self.assertEqual(v,'bar2')
        v=tm.get('foo',5)
        self.assertEqual(v,'bar2')


if __name__ == '__main__':
    unittest.main()