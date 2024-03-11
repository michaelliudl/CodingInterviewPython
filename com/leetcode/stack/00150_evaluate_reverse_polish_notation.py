from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens or len(tokens)==0:
            return -1
        st=list()
        for c in tokens:
            if not c in ['+','-','*','/']:
                st.append(c)
            elif len(st)<2:
                return -1
            elif c=='+':
                st.append(int(st.pop())+int(st.pop()))
            elif c=='-':
                st.append(-(int(st.pop())-int(st.pop())))
            elif c=='*':
                st.append(int(st.pop())*int(st.pop()))
            elif c=='/':
                b=int(st.pop())
                if b==0:
                    return -1
                st.append(int(int(st.pop())/b))
        if len(st)==1:
            return int(st[0])
        return -1

import unittest

class TestSolution(unittest.TestCase):
    def testEvalRPN(self):
        s = Solution()
        self.assertEqual(s.evalRPN(["2","1","+","3","*"]), 9)
        self.assertEqual(s.evalRPN(["4","13","5","/","+"]), 6)
        self.assertEqual(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]), 22)


if __name__ == '__main__':
    unittest.main()