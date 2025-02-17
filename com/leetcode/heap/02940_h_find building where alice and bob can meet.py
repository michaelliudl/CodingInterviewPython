from typing import List, DefaultDict
import heapq

class Solution:

    # Process `queries` into mapping 'right index' -> (larger value at two query indexes, original index in queries),
    # Except for queries can get result immediately, 1) same start location, 2) right start location has larger value
    # Then scan `heights`, for each index, use a min heap to store the query group
    # If the current height is larger than heap top's value, current height index is the answer to the heap top's query index
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        res = [-1] * len(queries)

        queryGroups = DefaultDict(list)
        for queryIndex, [query1, query2] in enumerate(queries):
            if query1 == query2:    # Same start location
                res[queryIndex] = query1
                continue
            rightQueryIndex = max(query1, query2)
            maxQueryHeight = max(heights[query1], heights[query2])
            # Right start location is meeting point
            if heights[query1] != heights[query2] and maxQueryHeight == heights[rightQueryIndex]:
                res[queryIndex] = rightQueryIndex
                continue
            
            queryGroups[rightQueryIndex].append((maxQueryHeight, queryIndex))

        heap = []
        for i, height in enumerate(heights):
            if i in queryGroups:
                for queryGroup in queryGroups[i]:
                    heapq.heappush(heap, queryGroup)
            while heap and height > heap[0][0]:
                res[heap[0][1]] = i
                heapq.heappop(heap)
            
        return res
    
    # Brute force
    def leftmostBuildingQueriesBrute(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        res = [-1] * len(queries)
        for queryIndex, [query1, query2] in enumerate(queries):
            if query1 == query2:    # Same start location
                res[queryIndex] = query1
                continue
            rightQueryIndex = max(query1, query2)
            maxQueryHeight = max(heights[query1], heights[query2])
            # Right start location is meeting point
            if heights[query1] != heights[query2] and maxQueryHeight == heights[rightQueryIndex]:
                res[queryIndex] = rightQueryIndex
                continue
            for i in range(rightQueryIndex + 1, len(heights)):
                if heights[i] > maxQueryHeight:
                    res[queryIndex] = i
                    break
        return res



import unittest

class TestSolution(unittest.TestCase):
    def testLeftmostBuildingQueries(self):
        s = Solution()
        self.assertEqual(s.leftmostBuildingQueries(heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]), 
                         [2,5,-1,5,2])
        self.assertEqual(s.leftmostBuildingQueries(heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]), 
                         [7,6,-1,4,6])
        self.assertEqual(s.leftmostBuildingQueries(heights = [1,2,1,2,1,2], queries = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[2,0],[2,1],[2,2],[2,3],[2,4],[2,5],[3,0],[3,1],[3,2],[3,3],[3,4],[3,5],[4,0],[4,1],[4,2],[4,3],[4,4],[4,5],[5,0],[5,1],[5,2],[5,3],[5,4],[5,5]]), 
                         [0,1,3,3,5,5,1,1,-1,-1,-1,-1,3,-1,2,3,5,5,3,-1,3,3,-1,-1,5,-1,5,-1,4,5,5,-1,5,-1,5,5])



if __name__ == '__main__':
    unittest.main()