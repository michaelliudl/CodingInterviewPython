from typing import List

'''
You are given two integer arrays nums1 and nums2 where nums2 is an anagram of nums1. Both arrays may contain duplicates.

Return an index mapping array mapping from nums1 to nums2 where mapping[i] = j means the ith element in nums1 appears in nums2 at index j. If there are multiple answers, return any of them.

An array a is an anagram of an array b means b is made by randomizing the order of the elements in a.



'''

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) != len(nums2):
            return []
        numMap = {}
        for index, num in enumerate(nums2):
            if num not in numMap:
                numMap[num] = []
            numMap[num].append(index)
        result = [-1] * len(nums1)
        for index, num in enumerate(nums1):
            if num in numMap and numMap[num]:
                result[index] = numMap[num].pop()
        return result
    
import unittest

class TestSolution(unittest.TestCase):
    def testAnagramMappings(self):
        s = Solution()
        self.assertEqual(s.anagramMappings(nums1 = [12,28,46,32,50], nums2 = [50,12,32,46,28]), [1,4,3,2,0])
        self.assertEqual(s.anagramMappings(nums1 = [84,46], nums2 = [84,46]), [0,1])
        

if __name__ == '__main__':
    unittest.main()
