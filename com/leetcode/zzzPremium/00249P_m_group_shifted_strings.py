from typing import List

'''
We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.
'''

class Solution:

    # Group by length first, then by diff of chars in string
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        def group(strs):
            groupByDiff = {}
            for string in strs:
                diffs = [0] * (len(string) - 1)
                for i in range(1, len(string)):
                    diff = (ord(string[i]) - ord(string[i - 1])) if string[i] > string[i - 1] else (ord(string[i]) + 26 - ord(string[i - 1]))
                    diffs[i - 1] = diff
                tupleDiffs = tuple(diffs)
                if tupleDiffs not in groupByDiff:
                    groupByDiff[tupleDiffs] = []
                groupByDiff[tupleDiffs].append(string)
            return groupByDiff

        if not strings:
            return []
        groupByLen = {}
        for string in strings:
            if len(string) not in groupByLen:
                groupByLen[len(string)] = []
            groupByLen[len(string)].append(string)
        result = []
        for strLen, strs in groupByLen.items():
            if strLen == 1 or len(strs) == 1:
                result.append(strs)
            else:
                groupByDiff = group(strs)
                for gDiff in groupByDiff.values():
                    result.append(gDiff)
        return result


import unittest

class TestSolution(unittest.TestCase):
    def testGroupStrings(self):
        s = Solution()
        self.assertEqual(s.groupStrings(strings = ["abc","bcd","acef","xyz","az","ba","a","z"]), 
                         [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]])
        self.assertEqual(s.groupStrings(strings = ["a"]), ["a"])


if __name__ == '__main__':
    unittest.main()