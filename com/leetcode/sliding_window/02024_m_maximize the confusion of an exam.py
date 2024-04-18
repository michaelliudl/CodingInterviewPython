from typing import List

class Solution:

    # One pass by tracking max count of T or F before current index.
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        result = 0
        left = 0
        maxCount = 0
        counts = {'T': 0, 'F': 0}
        for index, key in enumerate(answerKey):
            counts[key] += 1
            maxCount = max(maxCount, counts[key])
            while maxCount + k < (index - left + 1):
                counts[answerKey[left]] -= 1
                left += 1
            result = max(result, (index - left + 1))
        return result

    # Two pass to find max for T and F respectively
    def maxConsecutiveAnswers1(self, answerKey: str, k: int) -> int:

        def sliding(target, k):
            result = left = 0
            counter = k
            for index, key in enumerate(answerKey):
                if key == target:
                    counter -= 1
                while counter < 0:
                    if answerKey[left] == target:
                        counter += 1
                    left += 1
                result = max(result, (index - left + 1))
            return result

        if not answerKey:
            return 0
        resultT = sliding('T', k)
        resultF = sliding('F', k)
        return max(resultT, resultF)



import unittest

class TestSolution(unittest.TestCase):
    def testLongestOnes(self):
        s = Solution()
        self.assertEqual(s.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2), 6)
        self.assertEqual(s.longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3), 10)


if __name__ == '__main__':
    unittest.main()