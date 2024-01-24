from typing import List
import heapq

class Solution:


    # Monotonic array to calculate # of elements greater than arr[i] forwards and backwards
    def sumSubarrayMins(self, arr: List[int]) -> int:
        if not arr:
            return 0
        forward,backward=[0]*len(arr),[0]*len(arr)
        st=[]

        # Calculate # of elements to left of arr[i] that's greater or equal to it
        for i in range(len(arr)):
            while st and arr[i] < arr[st[-1]]:
                st.pop()
            forward[i] = (i - st[-1]) if st else i+1
            st.append(i)

        st=[]

        # Calculate # of elements to right of arr[i] that's greater than it
        for i in range(len(arr)-1, -1, -1):
            while st and arr[i] <= arr[st[-1]]:
                st.pop()
            backward[i] = (st[-1] - i) if st else (len(arr) - i)
            st.append(i)

        #Calculate sum of minimums of each subarray
        r=0
        for i in range(len(arr)):
            r = (r + arr[i] * forward[i] * backward[i]) % (10**9 + 7)
        return r

    # O(n**2)
    def sumSubarrayMinsBrute(self, arr: List[int]) -> int:
        if not arr:
            return 0
        r=0
        for i in range(len(arr)):
            st=[arr[i]]
            r+=st[0]
            for j in range(i+1, len(arr)):
                while st and arr[j]<st[-1]:
                    st.pop()
                st.append(arr[j])
                r+=st[0]
        return r%(10**9+7)

            


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