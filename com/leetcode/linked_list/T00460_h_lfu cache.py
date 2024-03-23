from typing import List
import heapq

class ListNode:


class LinkedList:

# Use doubly linked list to maintain frequency
class LFUCache:

class Node:

    def __init__(self, key = 0, value = 0, frequency = 0, accessOrder = 0):
        self.key = key
        self.value = value
        self.frequency = frequency
        self.accessOrder = accessOrder

    def __lt__(self, other):
        return (self.frequency < other.frequency) or (self.frequency == other.frequency and self.accessOrder < other.accessOrder)

# Use hash table to maintain key mapping to [value, access frequency, access order]
# Use an instance counter to track all access orders
# User min heap to track LFU (LRU if same frequency) with [frequency, access order, key].
# Time out
class LFUCache1:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.accessOrder = 0
        self.heap = []

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            node.frequency += 1
            self.accessOrder += 1
            node.accessOrder = self.accessOrder
            heapq.heapify(self.heap)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            node.frequency += 1
            self.accessOrder += 1
            node.accessOrder = self.accessOrder
            heapq.heapify(self.heap)
        else:
            while len(self.cache) >= self.capacity:
                node = heapq.heappop(self.heap)
                if node.key in self.cache:
                    del self.cache[node.key]
            self.accessOrder += 1
            node = Node(key, value, frequency=1, accessOrder=self.accessOrder)
            self.cache[key] = node
            heapq.heappush(self.heap, node)


class Solution:
    pass


import unittest

class TestSolution(unittest.TestCase):
    def testLFUCache(self):
        cache = LFUCache(capacity=2)
        cache.put(key=1, value=1)
        cache.put(key=2, value=2)
        self.assertEqual(cache.get(key=1), 1)
        cache.put(key=3, value=3)
        self.assertEqual(cache.get(key=2), -1)
        self.assertEqual(cache.get(key=3), 3)
        cache.put(key=4, value=4)
        self.assertEqual(cache.get(key=1), -1)
        self.assertEqual(cache.get(key=3), 3)
        self.assertEqual(cache.get(key=4), 4)


if __name__ == '__main__':
    unittest.main()