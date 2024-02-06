from typing import List

class Solution:

    def compress(self, chars: List[str]) -> int:
        if not chars: return 0
        if len(chars)==1: return 1
        slow,fast,ans,n=0,1,1,len(chars)
        curPos,curChar=0,chars[0]
        while fast<=n:
            if fast==n or chars[fast]!=curChar:
                count=fast-slow
                slow=fast
                if fast<n:
                    curChar=chars[fast]
                if count>1:
                    st=[]
                    while count>0:
                        st.append(str(count % 10))
                        count //= 10
                    while st:
                        element=st.pop()
                        curPos+=1
                        chars[curPos]=element
                        ans+=1
                if fast<n:
                    curPos+=1
                    chars[curPos]=curChar
                    ans+=1
                else: break
            else:
                fast+=1
        return ans


import unittest

class TestSolution(unittest.TestCase):

    def testCompress(self):
        s = Solution()
        chars = ["a","a","b","b","c","c","c"]
        self.assertEqual(s.compress(chars), 6)
        self.assertEqual(chars[:6], ["a","2","b","2","c","3"])
        chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
        self.assertEqual(s.compress(chars), 4)
        self.assertEqual(chars[:4], ["a","b","1","2"])

if __name__ == '__main__':
    unittest.main()