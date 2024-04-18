from typing import List
import heapq

class Solution:

    # Sum of min value in the subarrays.
    # Same as 84 largest rectangle in histogram. Think about array values as heights.
    def sumSubarrayMins1(self, arr: List[int]) -> int:
        if not arr:
            return 0
        arr = [0] + arr + [0]
        ret = 0
        stack = []
        for i, num in enumerate(arr):
            while stack and num < arr[stack[-1]]:
                midIndex = stack.pop()
                midValue = arr[midIndex]
                left = midIndex - stack[-1]     # Guranteed since prefixed `arr` with 0
                right = i - midIndex
                ret += midValue * left * right
                ret %= (10 ** 9 + 7)
            stack.append(i)
        return ret


    # Equivalent to find sum of ((each element) * (number of subarrays with this element as min element))
    # Number of subarrays with current element as min = (Number of subarrays before current (inclusive) element and with it as min) * (Number of subarrays after current (inclusive) element and with it as min)
    # Use one array to track index of first element before current and smaller, use Monotonic stack to find it
    # Use another array to track index of first elements after current and smaller than or equal to current, use Monotonic stack to find it
    def sumSubarrayMins(self, arr: List[int]) -> int:
        if not arr:
            return 0
        n = len(arr)
        prevSmaller = [-1] * n  # First index before `i` with value smaller than arr[i]
                                # Initialized with -1 in case smaller index doesn't exist on prev
        stack = []      # Monotonic increasing stack, since to find smaller elements' index
        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:    # Only pop smaller, stops at first same/smaller value on prev side
                stack.pop()
            if stack:
                prevSmaller[i] = stack[-1]
            stack.append(i)

        nextSmaller = [n] * n   # First index after `i` with value smaller than or equal to arr[i]. 
                                # Only include `equals` on `next` side to avoid duplicate subarrays being considered when multiple indexes with same value
                                # Initialized with `n` in case smaller index doesn't exist on after
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[i] <= arr[stack[-1]]:   # Pop smaller and equal, stops at first smaller on next side
                stack.pop()
            if stack:
                nextSmaller[i] = stack[-1]
            stack.append(i)
        
        res = 0
        for i in range(n):
            # Number of subarrays with arr[i] as min, before `i` and after `i`
            res += arr[i] * (i - prevSmaller[i]) * (nextSmaller[i] - i)
            res %= (10 ** 9 + 7)
        return res

    # def sumSubarrayMins2(self, arr: List[int]) -> int:
    #     if not arr:
    #         return 0
    #     forward,backward=[0]*len(arr),[0]*len(arr)
    #     st=[]

    #     # Calculate # of elements to left of arr[i] that's greater or equal to it
    #     for i in range(len(arr)):
    #         while st and arr[i] < arr[st[-1]]:
    #             st.pop()
    #         forward[i] = (i - st[-1]) if st else i+1
    #         st.append(i)

    #     st=[]

    #     # Calculate # of elements to right of arr[i] that's greater than it
    #     for i in range(len(arr)-1, -1, -1):
    #         while st and arr[i] <= arr[st[-1]]:
    #             st.pop()
    #         backward[i] = (st[-1] - i) if st else (len(arr) - i)
    #         st.append(i)

    #     #Calculate sum of minimums of each subarray
    #     r=0
    #     for i in range(len(arr)):
    #         r = (r + arr[i] * forward[i] * backward[i]) % (10**9 + 7)
    #     return r

    # O(n**2), TLE
    def sumSubarrayMinsBrute(self, arr: List[int]) -> int:
        if not arr:
            return 0
        ret = 0
        for i in range(len(arr)):
            ret += arr[i]
            curMin = arr[i]
            for j in range(i + 1, len(arr)):
                curMin = min(curMin, arr[j])
                ret += curMin
        return ret % (10**9 + 7)

            


    # O(n**2 * log(n)) Timeout
    def sumSubarrayMinsHeap(self, arr: List[int]) -> int:

        if not arr:
            return 0
        r,n=0,len(arr)
        for i in range(n):
            h=[]
            heapq.heappush(h, arr[i])
            r+=h[0]
            for j in range(i+1,n):
                heapq.heappush(h, arr[j])
                r+=h[0]
        return r%(10**9+7)

        

import unittest

class TestSolution(unittest.TestCase):
    def testSumSubarrayMins(self):
        s = Solution()
        self.assertEqual(s.sumSubarrayMins(arr = [3,1,2,4]), 17)
        self.assertEqual(s.sumSubarrayMins(arr = [11,81,94,43,3]), 444)
        


if __name__ == '__main__':
    unittest.main()