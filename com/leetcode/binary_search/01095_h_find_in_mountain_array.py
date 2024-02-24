from typing import List

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:

        # Start with high=n-1 to avoid getting out of range
        def peak():
            low,high = 0,n-1
            while low <= high:
                mid = low + (high - low) // 2
                midVal = mountain_arr.get(mid)
                beforeVal = mountain_arr.get(mid-1)
                afterVal = mountain_arr.get(mid+1)
                if midVal > beforeVal and midVal > afterVal:
                    return (mid, midVal)
                elif midVal > beforeVal:
                    low = mid+1
                else:
                    high = mid
        
        def search(low, high, leftOfPeak):
            while low < high:
                mid = low + (high - low) // 2
                midVal = mountain_arr.get(mid)
                if midVal == target:
                    return mid
                elif midVal > target:
                    if leftOfPeak:
                        high = mid
                    else:
                        low = mid + 1
                else:
                    if leftOfPeak:
                        low = mid + 1
                    else:
                        high = mid
            return -1

        n = mountain_arr.length()
        peakIndex,peakVal = peak()
        if peakVal == target:
            return peakIndex
        ans = search(0, peakIndex, leftOfPeak=True)
        if ans == -1:
            ans = search(peakIndex, n, leftOfPeak=False)
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