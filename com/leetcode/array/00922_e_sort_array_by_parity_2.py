from typing import List

class Solution:

    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        if not nums: return []
        evenIndex=0
        for i in range(1,len(nums),2):
            if nums[i]%2==0:
                while nums[evenIndex]%2==0:
                    evenIndex+=2
                nums[i],nums[evenIndex]=nums[evenIndex],nums[i]
        return nums

    def sortArrayByParityIITwoPointer(self, nums: List[int]) -> List[int]:

        def parity(i):
            return oddParity(i) or evenParity(i)
        
        def evenParity(i):
            return (i%2==0 and nums[i]%2==0)

        def oddParity(i):
            return (i%2==1 and nums[i]%2==1)
        
        def sameNoParity(i,j):
            return (oddIndexNoP(i) and oddIndexNoP(j)) or (evenIndexNoP(i) and evenIndexNoP(j))
        
        def oddIndexNoP(i):
            return (i%2==1 and nums[i]%2==0)
        
        def evenIndexNoP(i):
            return (i%2==0 and nums[i]%2==1)

        if not nums: return []
        low,high=0,len(nums)-1
        while low<high:
            if parity(low) and parity(high):
                low+=1
                high-=1
            elif parity(low):
                low+=1
            elif parity(high):
                high-=1
            elif not sameNoParity(low,high):
                nums[low],nums[high]=nums[high],nums[low]
            else:
                for i in range(low+1,high):
                    if not parity(i) and not sameNoParity(low,i):
                        nums[low],nums[i]=nums[i],nums[low]
                        break
        return nums

        

import unittest

class TestSolution(unittest.TestCase):

    def testSortArrayByParityII(self):
        s=Solution()
        # self.assertEqual(s.sortArrayByParityII(nums = [4,2,5,7]), [4,5,2,7])
        # self.assertEqual(s.sortArrayByParityII(nums = [2,3]), [2,3])
        self.assertEqual(s.sortArrayByParityII(nums = [2,3,1,1,4,0,0,4,3,3]), [2,3,0,1,4,1,0,3,4,3])

if __name__ == '__main__':
    unittest.main()