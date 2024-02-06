from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs: return [str]
        map = {}
        for string in strs:
            charOccur = [0]*26
            for c in string:
                charOccur[ord(c)-ord('a')] += 1
            key = ','.join([str(e) for e in charOccur])
            if key in map:
                map[key].append(string)
            else:
                map[key] = [string]
        ans = []
        for _,v in map.items():
            ans.append(v)
        return ans

import unittest

class TestSolution(unittest.TestCase):
    def testGroupAnagrams(self):
        s = Solution()
        # self.assertEqual(s.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]), [["bat"],["nat","tan"],["ate","eat","tea"]])
        self.assertEqual(s.groupAnagrams(strs = ["bdddddddddd","bbbbbbbbbbc"]), [["bbbbbbbbbbc"],["bdddddddddd"]])

if __name__ == '__main__':
    unittest.main()