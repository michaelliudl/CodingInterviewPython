from typing import List,Deque

class Solution:

    def continuousSubarrays(self, nums: List[int]) -> int:
        if not nums: return 0
        ans = 0
        curMap = {nums[0]: 1}
        curMin, curMax = nums[0], nums[0]
        queue = Deque()
        queue.append((nums[0], 0))
        for i in range(1,len(nums)):
            cur = nums[i]
            if abs(cur - curMin) > 2 or abs(cur - curMax) > 2:
                while queue:
                    if abs(cur - curMin) <= 2 and abs(cur - curMax) <= 2:
                        break
                    value, index = queue.popleft()
                    ans += (i - index)
                    curMap[value] -= 1
                    if curMap[value] == 0:
                        if value == curMin:
                            if value + 1 in curMap:
                                curMin = value + 1
                            elif value + 2 in curMap:
                                curMin = value + 2
                            else:
                                curMin = cur
                        if value == curMax:
                            if value - 1 in curMap:
                                curMax = value - 1
                            elif value - 2 in curMap:
                                curMax = value - 2
                            else:
                                curMax = cur
            queue.append((cur, i))
            if cur in curMap:
                curMap[cur] += 1
            else:
                curMap[cur] = 1
            curMin = min(curMin, cur)
            curMax = max(curMax, cur)
        while queue:
            _, index = queue.popleft()
            ans += (len(nums) - index)
        return ans

    # O(n**2)
    def continuousSubarraysBrute(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        ans = n
        for i in range(n-1):
            curMax, curMin = nums[i], nums[i]
            for j in range(i+1, n):
                if (abs(curMax - nums[j]) > 2) or (abs(curMin - nums[j]) > 2):
                    break
                ans += 1
                curMax = max(curMax, nums[j])
                curMin = min(curMin, nums[j])
        return ans




import unittest

class TestSolution(unittest.TestCase):
    def testContinuousSubarrays(self):
        s = Solution()
        self.assertEqual(s.continuousSubarrays(nums = [1,1,1,1,1000000000,1000000000,1000000000,1000000000]), 20)
        self.assertEqual(s.continuousSubarrays(nums = [94,95,96,96,97,98,99,100,100]), 28)
        self.assertEqual(s.continuousSubarrays(nums = [5,4,2,4]), 8)
        self.assertEqual(s.continuousSubarrays(nums = [1,2,3]), 6)
        self.assertEqual(s.continuousSubarrays(nums = [35,35,36,37,36,37,38,37,38]), 39)

if __name__ == '__main__':
    unittest.main()