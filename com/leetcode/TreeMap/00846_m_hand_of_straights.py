from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if not hand or not len(hand) % groupSize == 0:
            return False
        map = {}
        for card in hand:
            map[card] = map.get(card, 0) + 1
        while map:
            minKey = min(map.keys())
            for i in range(groupSize):
                key = minKey + i
                if key not in map:
                    return False
                map[key] -= 1
                if map[key] == 0:
                    del map[key]
        return True
    
import unittest

class TestSolution(unittest.TestCase):
    def testIsNStraightHand(self):
        s = Solution()
        self.assertEqual(s.isNStraightHand(hand = [1,2,3,6,2,3,4,7,8], groupSize = 3), True)
        self.assertEqual(s.isNStraightHand(hand = [1,2,3,4,5], groupSize = 4), False)


if __name__ == '__main__':
    unittest.main()