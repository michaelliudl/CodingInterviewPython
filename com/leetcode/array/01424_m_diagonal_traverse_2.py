from typing import List

class Solution:

    # Each diagonal has same number from adding original row and column.
    # Scan and cache diagonal number and list elements in map. Elements are added in reverse order per requirement.
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        if not nums:
            return []
        map = {}
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                key = i + j
                if key not in map:
                    map[key] = []
                map[key].append(nums[i][j])
        diagonals = []
        for k, v in map.items():
            diagonals.append((k, reversed(v)))
        diagonals.sort()
        ans = []
        for _, diag_nums in diagonals:
            ans.extend(diag_nums)
        return ans


    # Time out. Simulate by moving row and column index m*n times
    def findDiagonalOrderSim(self, nums: List[List[int]]) -> List[int]:
        if not nums:
            return []
        ans = []
        for row in range(len(nums)):
            for col in range(row + 1):
                if col < len(nums[row - col]):
                    ans.append(nums[row - col][col])
        maxCol = max([len(row) for row in nums])
        for col in range(1, maxCol):
            for row in range(len(nums) - 1, -1, -1):
                curCol = col + (len(nums) - 1 - row)
                if curCol < len(nums[row]):
                    ans.append(nums[row][curCol])
        return ans
    
import unittest

class TestSolution(unittest.TestCase):
    def testFindDiagonalOrder(self):
        s = Solution()
        self.assertEqual(s.findDiagonalOrder(nums = [[1,2,3],[4,5,6],[7,8,9]]), [1,4,2,7,5,3,8,6,9])
        self.assertEqual(s.findDiagonalOrder(nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]), [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16])

if __name__ == '__main__':
    unittest.main()