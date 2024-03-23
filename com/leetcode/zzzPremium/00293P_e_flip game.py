from typing import List
'''
You are playing a Flip Game with your friend.

You are given a string currentState that contains only '+' and '-'. You and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move, and therefore the other person will be the winner.

Return all possible states of the string currentState after one valid move. You may return the answer in any order. If there is no valid move, return an empty list [].
'''

class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        if not currentState or len(currentState) < 2:
            return []
        result = []
        for i in range(1, len(currentState)):
            if currentState[i - 1] == currentState[i] == '+':
                result.append(currentState[:i - 1] + '--' + currentState[i + 1:])
        return result
    
import unittest

class TestSolution(unittest.TestCase):
    def testGeneratePossibleNextMoves(self):
        s = Solution()
        self.assertEqual(s.generatePossibleNextMoves(currentState = "++++"), ["--++","+--+","++--"])
        self.assertEqual(s.generatePossibleNextMoves(currentState = "+"), [])


if __name__ == '__main__':
    unittest.main()
