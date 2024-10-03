from typing import List, Counter

class Solution:

    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]: 
        counts1 = Counter(s1.split(' ')) 
        counts2 = Counter(s2.split(' ')) 
        res = [] 
        for word, count in counts1.items(): 
            if count == 1 and word not in counts2: 
                res.append(word) 
        for word, count in counts2.items(): 
            if count == 1 and word not in counts1: 
                res.append(word) 
        return res
                       


import unittest

class TestSolution(unittest.TestCase):
    def testIsLongPressedName(self):
        s = Solution()
        self.assertEqual(s.isLongPressedName(name = "alex", typed = "aaleexx"), True)
        self.assertEqual(s.isLongPressedName(name = "alex", typed = "aaleexxxxx"), True)
        self.assertEqual(s.isLongPressedName(name = "saeed", typed = "ssaaedd"), False)
        self.assertEqual(s.isLongPressedName(name = "leelee", typed = "lleeelee"), True)
        self.assertEqual(s.isLongPressedName(name = "alex", typed = "aaleexabc"), False)
        self.assertEqual(s.isLongPressedName(name = "alexabc", typed = "aaleexxxxxx"), False)


if __name__ == '__main__':
    unittest.main()