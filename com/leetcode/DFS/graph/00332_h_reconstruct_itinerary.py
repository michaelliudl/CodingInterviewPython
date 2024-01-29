from typing import List,Deque

class Solution:

    # DFS by creating graph first
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        def dfs(start):
            while start in graph and graph[start]:
                dest=graph[start].pop(0)
                dfs(dest)
            path.append(start)

        if not tickets: return []
        graph,path={},[]
        for s,e in tickets:
            if not s in graph:
                graph[s]=[e]
            else:
                graph[s].append(e)
                
        for _,v in graph.items():
            v.sort()
        dfs(start='JFK')
        l,r=0,len(path)-1
        while l<r:
            path[l],path[r]=path[r],path[l]
            l+=1
            r-=1
        return path
        


    # Time out
    def findItineraryDFS(self, tickets: List[List[str]]) -> List[str]:

        def dfs(start):
            nonlocal r,found
            if len(used)==n:
                r=path[:]
                found=True
                return
            for i in range(n):
                if not found and not i in used:
                    s,e=tickets[i]
                    if s==start:
                        path.append(e)
                        used[i]=1
                        dfs(e)
                        del used[i]
                        path.pop()

        if not tickets: return []
        tickets.sort()
        used,n={},len(tickets)
        path,r,found=['JFK'],[],False
        dfs(start='JFK')
        return r

    # Backtrack time out on test case #81
    def findItineraryBacktrack(self, tickets: List[List[str]]) -> List[str]:
        def backtrack(tickets, used, path):
            if sum(used)==len(tickets):
                return path
            start=path[-1]
            for i,v in enumerate(tickets):
                if used[i]:
                    continue
                if v[0]==start:
                    end=v[1]
                    endIndex=i
                    path.append(end)
                    used[endIndex]=1
                    r=backtrack(tickets, used, path)
                    if r:
                        return r
                    path.pop()
                    used[endIndex]=0
            return []

        if not tickets:
            return []
        # Sort, then first valid path is lexical smallest
        tickets.sort()
        used=[0]*len(tickets)
        path=['JFK']
        backtrack(tickets, used, path)
        return path

import unittest

class TestSolution(unittest.TestCase):
    def testFindItinerary(self):
        s = Solution()
        self.assertEqual(s.findItinerary(tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]), 
                         ["JFK","MUC","LHR","SFO","SJC"])
        self.assertEqual(s.findItinerary(tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]),
                         ["JFK","ATL","JFK","SFO","ATL","SFO"])
        self.assertEqual(s.findItinerary(tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]),
                         ["JFK","NRT","JFK","KUL"])
        self.assertEqual(s.findItinerary(tickets = [['AAA', 'BBB'], ['ATL', 'AAA'], ['BBB', 'ATL'], ['JFK', 'ATL'], ['JFK', 'SFO'], ['SFO', 'JFK']]),
                         ['JFK', 'SFO', 'JFK', 'ATL', 'AAA', 'BBB', 'ATL'])
        self.assertEqual(s.findItinerary(tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","JFK"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"]]),
                         ["JFK","SFO","JFK","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL","AAA","BBB","ATL"])
        


if __name__ == '__main__':
    unittest.main()