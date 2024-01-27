from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def isValidIPNum(s):
            if len(s)>3:
                return False
            if len(s)>1 and s[0]=='0':
                return False
            if int(s)>255:
                return False
            return True
        
        def backtrack(s, startIndex, r, path):
            if len(path)==4:
                if startIndex==len(s):
                    r.append('.'.join(path))
                return
            for i in range(startIndex, len(s)):
                # Check remaining string is a valid fourth IP number
                if len(path)==3:
                    if isValidIPNum(s[startIndex:]):
                        path.append(s[startIndex:])
                        backtrack(s, len(s), r, path)
                        path.pop()
                    break
                else:
                    prefix=s[startIndex : i+1]
                    if not isValidIPNum(prefix):
                        continue
                    path.append(prefix)
                    backtrack(s, i+1, r, path)
                    path.pop()

        if not s or len(s)<4:
            return []
        r=[]
        backtrack(s, startIndex=0, r=r, path=[])
        return r

        

import unittest

class TestSolution(unittest.TestCase):
    def testRestoreIpAddresses(self):
        s = Solution()
        self.assertEqual(s.restoreIpAddresses(s = "25525511135"), ["255.255.11.135","255.255.111.35"])
        self.assertEqual(s.restoreIpAddresses(s = "0000"), ["0.0.0.0"])
        self.assertEqual(s.restoreIpAddresses(s = "101023"), ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"])


if __name__ == '__main__':
    unittest.main()