from typing import List

class Solution:

    # Hash O(n) space
    # 
    # Boyer-Moore's Voting Algorithm O(1) space
    # 1. If the current element is equal to one of the candidates, increment the count for that candidate.
    # 2. If the count for one of the candidates reaches zero, update that candidate to the current element and set its count to 1.
    # 3. If the current element is different from both candidates, decrement the counts for both candidates.
    # 4. After iterating through the array, we need to verify the actual counts of the potential majority elements. We'll iterate through the array again and count the occurrences of each potential majority element. If the count exceeds ⌊ n/3 ⌋, we add the element to the result.
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums: return []
        candidate1,candidate2=None,None
        count1,count2=0,0
        for num in nums:
            if num==candidate1:
                count1+=1
            elif num==candidate2:
                count2+=1
            elif count1==0:
                candidate1=num
                count1=1
            elif count2==0:
                candidate2=num
                count2=1
            else:
                count1-=1
                count2-=1

        count1,count2=0,0
        for num in nums:
            if num==candidate1:
                count1+=1
            elif num==candidate2:
                count2+=1
        result,target=[],len(nums)//3
        if count1>target:
            result.append(candidate1)
        if count2>target:
            result.append(candidate2)
        return result
        

        

import unittest

class TestSolution(unittest.TestCase):

    def testPivotIndex(self):
        s=Solution()
        self.assertEqual(s.pivotIndex(nums = [1,7,3,6,5,6]), 3)
        self.assertEqual(s.pivotIndex(nums = [2,1,-1]), 0)
        self.assertEqual(s.pivotIndex(nums = [1,2,3]), -1)

if __name__ == '__main__':
    unittest.main()