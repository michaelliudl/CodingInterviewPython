from typing import List, Deque

class Solution:

    # Simulation with queue. Almost time out
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks or n < 0: return 0
        cache={}
        for task in tasks:
            cache[task] = cache.get(task, 0) + 1
        cur={}
        q=Deque()
        ans=0
        while cache:
            while len(q) > n:               # Pop out first task after idle enough
                out = q.popleft()
                if out != '#':
                    del cur[out]
            next,nextCount=None,0
            for k,v in cache.items():
                if k not in cur and v >= nextCount:     # Greedily choose next task with most remaining cout
                    next = k
                    nextCount = v
            if next: 
                cache[next] -= 1
                if cache[next] == 0: del cache[next]
                cur[next] = 1
            else:
                next = '#'          # Placeholder for idle if no task can be chosen
            q.append(next)
            ans += 1
        return ans


import unittest

class TestSolution(unittest.TestCase):
    def testLeastInterval(self):
        s = Solution()
        self.assertEqual(s.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2), 8)
        self.assertEqual(s.leastInterval(tasks = ["A","A","A","B","B","B"], n = 0), 6)
        self.assertEqual(s.leastInterval(tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2), 16)
        self.assertEqual(s.leastInterval(tasks = ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"], n = 2), 12)



if __name__ == '__main__':
    unittest.main()