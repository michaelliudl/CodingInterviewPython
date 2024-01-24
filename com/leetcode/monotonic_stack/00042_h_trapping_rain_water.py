from typing import List
from typing import Deque


class Solution:

    # Monotonic stack to calculate each water area horizontally
    def trap(self, height: List[int]) -> int:
        if not height or len(height)<=2:
            return 0
        total,n,st=0,len(height),[0]
        for i in range(1,n):
            cur=height[i]
            while st and cur>=height[st[-1]]:
                midIdx=st.pop()
                mid=height[midIdx]
                if st:
                    leftIdx=st[-1]
                    left=height[leftIdx]
                    total+=(min(cur,left) - mid) * (i - leftIdx - 1)
            st.append(i)
        return total


    # Two pointer
    def trapTwoPointer(self, height: List[int]) -> int:
        if not height or len(height)<=2:
            return 0
        n=len(height)
        # Find highest to left of each
        highLeft = [0]*n
        highLeft[0] = height[0]
        for i in range(1,n):
            highLeft[i] = max(height[i], highLeft[i-1])

        # Find highest to right of each
        highRight = [0]*n
        highRight[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            highRight[i] = max(height[i], highRight[i+1])

        total = 0
        for i in range(n):
            water = min(highLeft[i], highRight[i]) - height[i]
            total += water if water > 0 else 0
        return total

    # Divide
    def trapDivide(self, height: List[int]) -> int:

        def calcF(prev,next,tallest):
            area=0
            while next<=tallest:
                if height[prev]==0:
                    prev+=1
                elif height[next]>=height[prev]:
                    area+=height[prev]*(next-prev-1) - sum(height[prev+1:next])
                    prev=next
                next+=1
            return area
        
        def calcB(prev,next,tallest):
            area=0
            while next>=tallest:
                if height[prev]==0:
                    prev-=1
                elif height[next]>=height[prev]:
                    area+=height[prev]*(prev-next-1) - sum(height[next+1:prev])
                    prev=next
                next-=1
            return area

        if not height:
            return 0
        tv=max(height)
        ti=[i for i,v in enumerate(height) if v==tv]
        total=0
        total+=calcF(prev=0, next=1, tallest=ti[0])
        if len(ti)>1:
            for i in range(len(ti)-1):
                total+=calcF(prev=ti[i],next=ti[i]+1,tallest=ti[i+1])
        total+=calcB(prev=len(height)-1,next=len(height)-2,tallest=ti[-1])
        return total
        
        
        



import unittest

class TestSolution(unittest.TestCase):
    def testTrap(self):
        s = Solution()
        self.assertEqual(s.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]), 6)
        self.assertEqual(s.trap(height = [4,2,0,3,2,5]), 9)



if __name__ == '__main__':
    unittest.main()