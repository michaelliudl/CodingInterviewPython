from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2: return []
        count1,count2 = {},{}
        for num in nums1:
            count1[num] = count1.get(num, 0) + 1
        for num in nums2:
            count2[num] = count2.get(num, 0) + 1
        ans = []
        for k,v in count1.items():
            if k in count2:
                for _ in range(min(v, count2[k])):
                    ans.append(k)
        return ans

import unittest

class TestSolution(unittest.TestCase):
    def testTwoSum(self):
        s = Solution()
        self.assertEqual(s.twoSum([2,7,11,15],9), [0,1])
        self.assertEqual(s.twoSum([3,2,4],6), [1,2])
        self.assertEqual(s.twoSum([3,3],6), [0,1])


if __name__ == '__main__':
    unittest.main()