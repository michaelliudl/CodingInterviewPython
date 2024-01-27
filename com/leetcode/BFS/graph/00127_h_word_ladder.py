from typing import List,Deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def bfs():
            nonlocal r,found
            q=Deque()
            q.append(beginWord)
            used[beginWord]=1
            while q:
                x=len(q)
                for _ in range(x):
                    word=q.popleft()
                    if word==endWord:
                        found=True
                        return
                    used[word]=1
                    if word in cache:
                        for w in cache[word]:
                            if not w in used:
                                used[w]=1
                                q.append(w)
                r+=1
                
            
        def close(w1,w2):
            diff=False
            for i in range(m):
                if w1[i]!=w2[i]:
                    if diff: return False
                    else: diff=True
            return diff

        def makeCache():
            for w1 in wordList:
                cache[w1]=[]
                for w2 in wordList:
                    if close(w1,w2):
                        cache[w1].append(w2)
            cache[beginWord]=[]
            for w in wordList:
                if close(beginWord,w):
                    cache[beginWord].append(w)
            

        if not endWord in wordList:
            return 0
        m,n,r=len(beginWord),len(wordList),1
        cache,used,found={},{},False
        makeCache()
        bfs()
        return r if found else 0



        

import unittest

class TestSolution(unittest.TestCase):
    def testLadderLength(self):
        s = Solution()
        # self.assertEqual(s.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]), 5)
        # self.assertEqual(s.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]), 0)
        self.assertEqual(s.ladderLength(beginWord = "hot", endWord = "dog", wordList = ["hot","dog"]), 0)
        


if __name__ == '__main__':
    unittest.main()