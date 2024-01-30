from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        dirs=[(-1,0),(1,0),(0,-1),(0,1)]

        def valid(x,y):
            return x>=0 and x<m and y>=0 and y<n

        def dfs(x, y, potentials, start, path):
            lenList=[len(p) for p in potentials]
            maxLen,minLen=max(lenList),min(lenList)
            if start>=minLen-1 and start<=maxLen-1:
                pass
                # pathWord=''.join(path)
                # if pathWord in potentials:
                #     result.append(pathWord)
                    # return
            if start==maxLen-1:
                pathWord=''.join(path)
                if pathWord in potentials:
                    result.append(pathWord)
                return
            visited[x][y]=True
            for dx,dy in dirs:
                nx,ny=x+dx,y+dy
                if valid(nx,ny) and not visited[nx][ny]:
                    if board[nx][ny] in [p[start+1] for p in potentials if start+1<len(p)]:
                        path.append(board[nx][ny])
                        dfs(nx,ny,[p for p in potentials if start+1<len(p) and p[start+1]==board[nx][ny]], start+1, path)
                        path.pop()
            visited[x][y]=False

        if not board or not words: return []
        m,n,k=len(board),len(board[0]),len(words)
        wordMap={}
        for w in words:
            if w[0] in wordMap:
                wordMap[w[0]].append(w)
            else:
                wordMap[w[0]]=[w]
        visited=[[False]*n for _ in range(m)]
        result=[]
        for i in range(m):
            for j in range(n):
                if board[i][j] in wordMap:
                    dfs(x=i, y=j, potentials=wordMap[board[i][j]], start=0, path=[board[i][j]])
        return result


import unittest

class TestSolution(unittest.TestCase):
    def testFindWords(self):
        s = Solution()
        self.assertEqual(s.findWords(board = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]], words = ["oa","oaa"]), ["oa","oaa"])
        # self.assertEqual(s.findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]), 
        #                  ["oath","eat"])
        # self.assertEqual(s.findWords(board = [["a","b"],["c","d"]], words = ["abcb"]), [])


if __name__ == '__main__':
    unittest.main()