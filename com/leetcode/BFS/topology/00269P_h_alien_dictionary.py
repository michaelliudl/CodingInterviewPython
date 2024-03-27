from typing import List,Deque,DefaultDict

class Solution:

    def alienOrder(self, words: List[str]) -> str:
        # 1. Build graph and in-degress of chars
        graph = {}
        inDeg = {char : 0 for word in words for char in word}
        for i in range(1, len(words)):
            prev, cur = words[i - 1], words[i]
            minLen = min(len(prev), len(cur))
            diffInMinLen = False
            for j in range(minLen):
                if prev[j] != cur[j]:
                    diffInMinLen = True
                    if prev[j] not in graph:
                        graph[prev[j]] = set()
                    if cur[j] not in graph[prev[j]]:
                        graph[prev[j]].add(cur[j])
                        inDeg[cur[j]] += 1              # In-degree for each character is at most 1
                    break               # No need to consider after first diff
            if not diffInMinLen and len(prev) > len(cur):
                return ''               # Invalid if shorter word is prefix but longer word comes first
        # 2. Topological sort
        result = []
        queue = Deque()
        for char, indegree in inDeg.items():    # Chars with 0 in-degree are potential start of graph
            if indegree == 0:
                queue.append(char)
        while queue:
            char = queue.popleft()
            result.append(char)
            if char in graph:
                for neighbor in graph[char]:
                    inDeg[neighbor] -= 1
                    if inDeg[neighbor] == 0:
                        queue.append(neighbor)
        # Invalid if not all chars are included in result
        if len(result) != len(inDeg):
            return ''
        return ''.join(result)

import unittest

class TestSolution(unittest.TestCase):
    def testAlienOrder(self):
        s = Solution()
        self.assertEqual(s.alienOrder(words = ["ac","ab","zc","zb"]), "azcb")
        self.assertEqual(s.alienOrder(words = ["ab","adc"]), "bdac")
        self.assertEqual(s.alienOrder(words = ["z","z"]), "z")
        self.assertEqual(s.alienOrder(words = ["zy","zx"]), "yxz")
        self.assertEqual(s.alienOrder(words = ["wrt","wrf","er","ett","rftt"]), "wertf")
        self.assertEqual(s.alienOrder(words = ["z","x"]), "zx")
        self.assertEqual(s.alienOrder(words = ["z","x","z"]), "")
        self.assertEqual(s.alienOrder(words = ["ac","ab","b"]), "acb")
        

if __name__ == '__main__':
    unittest.main()