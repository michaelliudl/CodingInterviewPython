from typing import List

class Solution:

    def partitionLabels(self, s: str) -> List[int]:
        if not s: return []
        d,n={},len(s)
        for i in range(n):
            c=s[i]
            d[c]=max(d[c],i) if c in d else i
        r,start,end=[],0,-1
        for i in range(n):
            if d[s[i]]>end:
                end=d[s[i]]
            if i==end:
                r.append((end-start+1))
                start,end=i+1,i
        return r


import unittest

class TestSolution(unittest.TestCase):
    def testPartitionLabels(self):
        s = Solution()
        self.assertEqual(s.partitionLabels(s = "ababcbacadefegdehijhklij"), [9,7,8])
        self.assertEqual(s.partitionLabels(s = "eccbbbbdec"), [10])
        self.assertEqual(s.partitionLabels(s = "caedbdedda"), [1,9])
        


if __name__ == '__main__':
    unittest.main()