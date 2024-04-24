from typing import List
import bisect, heapq

class Solution:

    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        if not people or not flowers:
            return []
        peopleWithIndex = [(p, i) for i, p in enumerate(people)]    # Keep original index of people
        peopleWithIndex.sort()      # Sort by people's time
        flowers.sort()              # Sort by flowers' start time
        res = [0] * len(people)
        endTime = []

        flowerIndex = 0
        # Loop people time asc
        for personTime, personIndex in peopleWithIndex:
            # Keep finding flowers start time before current person's time and put end time into heap
            while flowerIndex < len(flowers) and flowers[flowerIndex][0] <= personTime:
                heapq.heappush(endTime, flowers[flowerIndex][1])
                flowerIndex += 1
            # Remove end time before current person's time
            while endTime and endTime[0] < personTime:
                heapq.heappop(endTime)
            # `endTime` now holds flowers started before and end after current people's time
            res[personIndex] = len(endTime)
        return res

    # Separate start time and end time and sort both
    # Then use binary search to find start/end index of flowers that cover each people's time
    def fullBloomFlowersBinarySearch(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = [f[0] for f in flowers]
        ends = [f[1] for f in flowers]
        starts.sort()
        ends.sort()
        res = [0] * len(people)
        for i in range(len(people)):
            time = people[i]
            # For each person, find last index of start time after person's time, find first index of end time before person's time
            start = bisect.bisect_right(starts, time)
            end = bisect.bisect_left(ends, time)
            res[i] = start - end
        return res

    
import unittest

class TestSolution(unittest.TestCase):
    def testTwoSum(self):
        s = Solution()
        self.assertEqual(s.twoSum([2,7,11,15],9), [0,1])
        self.assertEqual(s.twoSum([3,2,4],6), [1,2])
        self.assertEqual(s.twoSum([3,3],6), [0,1])


if __name__ == '__main__':
    unittest.main()