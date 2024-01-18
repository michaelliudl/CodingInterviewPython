from typing import List,Deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def bfs():
            q=Deque()
            q.append(beginWord)
            path=[]
            while q:
                cur=q.popleft()
                path.append(cur)
                if cur==endWord:
                    path.append(cur)
                    return len(path)
                for i in range(n):
                    for j in range(ord('a'), ord('z')+1):
                        c=chr(j)
                        word=cur[:i]+c+cur[i+1:]
                        if word!=beginWord and c in cache[i] and word in cache[i][c] and not word in path:
                            q.append(word)
                            # path.append(word)
                # path.pop()


        def makeCache(wordList,cache):
            for i in range(n):
                cache[i]={} if not i in cache else cache[i]
                for w in wordList:
                    if not w[i] in cache[i]:
                        cache[i][w[i]]=[w]
                    else:
                        cache[i][w[i]].append(w)

        if not endWord in wordList:
            return 0
        n=len(beginWord)
        cache={}
        makeCache(wordList,cache=cache)
        return bfs()



        

import unittest

class TestSolution(unittest.TestCase):
    def testLadderLength(self):
        s = Solution()
        self.assertEqual(s.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]), 5)
        self.assertEqual(s.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]), 0)
        


if __name__ == '__main__':
    unittest.main()