from typing import List

'''
Run-length encoding is a compression algorithm that allows for an integer array nums with many segments of consecutive repeated numbers to be represented by a (generally smaller) 2D array encoded. Each encoded[i] = [vali, freqi] describes the ith segment of repeated numbers in nums where vali is the value that is repeated freqi times.

For example, nums = [1,1,1,2,2,2,2,2] is represented by the run-length encoded array encoded = [[1,3],[2,5]]. Another way to read this is "three 1's followed by five 2's".
The product of two run-length encoded arrays encoded1 and encoded2 can be calculated using the following steps:

Expand both encoded1 and encoded2 into the full arrays nums1 and nums2 respectively.
Create a new array prodNums of length nums1.length and set prodNums[i] = nums1[i] * nums2[i].
Compress prodNums into a run-length encoded array and return it.
You are given two run-length encoded arrays encoded1 and encoded2 representing full arrays nums1 and nums2 respectively. Both nums1 and nums2 have the same length. Each encoded1[i] = [vali, freqi] describes the ith segment of nums1, and each encoded2[j] = [valj, freqj] describes the jth segment of nums2.

Return the product of encoded1 and encoded2.

Note: Compression should be done such that the run-length encoded array has the minimum possible length.

 
'''
class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        if not encoded2:
            return encoded1
        prod = []
        i = j = 0
        while i < len(encoded1) and j < len(encoded2):
            num1, len1 = encoded1[i]
            num2, len2 = encoded2[j]
            if len1 == len2:
                prod.append([num1 * num2, len1])
                i += 1
                j += 1
            elif len1 > len2:
                prod.append([num1 * num2, len2])
                encoded1[i][1] -= len2
                j += 1
            else:
                prod.append([num1 * num2, len1])
                encoded2[j][1] -= len1
                i += 1
        while i < len(encoded1):
            prod.append(encoded1[i])
            i += 1
        if not prod:
            return prod
        result = [prod[0]]
        for k in range(1, len(prod)):
            if result[-1][0] == prod[k][0]:
                result[-1][1] += prod[k][1]
            else:
                result.append(prod[k])
        return result


import unittest

class TestSolution(unittest.TestCase):
    def testFindRLEArray(self):
        s = Solution()
        self.assertEqual(s.findRLEArray(encoded1 = [[1,3],[2,3]], encoded2 = [[6,3],[3,3]]), [[6,6]])
        self.assertEqual(s.findRLEArray(encoded1 = [[1,3],[2,1],[3,2]], encoded2 = [[2,3],[3,3]]), [[2,3],[6,1],[9,2]])


if __name__ == '__main__':
    unittest.main()