from typing import List, Counter, DefaultDict

class Solution:
    
    # Count max character frequency in words2
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        maxCounts = DefaultDict(int)
        for word in words2:
            counts = Counter(word)
            for char, count in counts.items():
                maxCounts[
                    char] = max(maxCounts[char], count)
        res = []
        for word in words1:
            counts1 = Counter(word)
            isUniversal = True
            for char, maxCount in maxCounts.items():
                if char not in counts1 or counts1[char] < maxCount:
                    isUniversal = False
                    break
            if isUniversal:
                res.append(word)
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testGroupAnagrams(self):
        s = Solution()
        # self.assertEqual(s.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]), [["bat"],["nat","tan"],["ate","eat","tea"]])
        self.assertEqual(s.groupAnagrams(strs = ["bdddddddddd","bbbbbbbbbbc"]), [["bbbbbbbbbbc"],["bdddddddddd"]])

if __name__ == '__main__':
    unittest.main()