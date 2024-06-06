from typing import List

class Solution:

    # TODO simplify code
    def commonChars(self, words: List[str]) -> List[str]:
        if not words or len(words)==0 or len(words[0])==0:
            return list()
        ld=list()
        for w in words:
            d=dict()
            for c in w:
                d[c]=d[c]+1 if c in d else 1
            ld.append(d)
        all=[str(chr(ord('a')+c)) for c in range(26)]
        fd=dict()
        for c in all:
            cv=0
            for d in ld:
                if c in d:
                    cv=d[c] if cv==0 else min(cv,d[c])
                else:
                    cv=0
                    break
            if cv>0:
                fd[c]=cv
        fl=list()
        for c in fd:
            for _ in range(fd[c]):
                fl.append(c)
        return fl

import unittest

class TestSolution(unittest.TestCase):
    def testCommonChars(self):
        s = Solution()
        self.assertEqual(s.commonChars(["bella","label","roller"]), ["e","l","l"])
        self.assertEqual(s.commonChars(["cool","lock","cook"]), ["c","o"])


if __name__ == '__main__':
    unittest.main()