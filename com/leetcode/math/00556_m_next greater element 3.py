from typing import List

class Solution:

    # Split number into array of each single digits
    # Use # 31 next permutation to find next number in the permutation
    def nextGreaterElement(self, n: int) -> int:

        def numToArr(n):
            arr = []
            while n:
                arr.append(n % 10)
                n //= 10
            arr.reverse()
            return arr

        def arrToNum(arr):
            result = 0
            for num in arr:
                result = result * 10 + num
            return result

        def nextPermutation():
            peakIndexFromEnd = len(arr) - 1
            for i in range(len(arr) - 1, 0, -1):
                if arr[i] <= arr[i - 1]:
                    peakIndexFromEnd = i - 1
                else:
                    break
            if peakIndexFromEnd > 0:
                for i in range(len(arr) - 1, peakIndexFromEnd - 1, -1):
                    if arr[i] > arr[peakIndexFromEnd - 1]:
                        arr[i], arr[peakIndexFromEnd - 1] = arr[peakIndexFromEnd - 1], arr[i]
                        break
            low, high = peakIndexFromEnd, len(arr) - 1
            while low < high:
                arr[low], arr[high] = arr[high], arr[low]
                low += 1
                high -= 1

        if n <= 0:
            return 1
        arr = numToArr(n)
        nextPermutation()
        result = arrToNum(arr)
        if result <= n or result >= 2 ** 31:    # 2147483648 = 2 ** 31 doesn't fit 32 bit signed int
            return -1
        return result


import unittest

class TestSolution(unittest.TestCase):
    def testNextGreaterElement(self):
        s = Solution()
        self.assertEqual(s.nextGreaterElement(12), 21)
        self.assertEqual(s.nextGreaterElement(21), -1)
        


if __name__ == '__main__':
    unittest.main()