from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        if not spells or not potions or success <=0: return []
        potions.sort()

        for i in range(len(spells)):
            target = (success // spells[i]) if (success % spells[i] == 0) else (success // spells[i] + 1)
            if target <= 0 or target > potions[-1]:
                spells[i] = 0
            low, high = 0, len(potions)
            while low < high:
                mid = low + (high - low) // 2
                if potions[mid] >= target:
                    high = mid
                else:
                    low = mid + 1
            spells[i] = len(potions) - low
        return spells
            

import unittest

class TestSolution(unittest.TestCase):
    def testSuccessfulPairs(self):
        s = Solution()
        self.assertEqual(s.successfulPairs(spells = [5,1,3], potions = [1,2,3,4,5], success = 7), [4,0,3])
        self.assertEqual(s.successfulPairs(spells = [3,1,2], potions = [8,5,8], success = 16), [2,0,2])


if __name__ == '__main__':
    unittest.main()