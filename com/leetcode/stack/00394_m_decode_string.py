from typing import Optional,List,Deque



class Solution:

    def decodeString(self, s: str) -> str:

        def digit(c):
            return c >= '0' and c <= '9'

        if not s: return s
        st=[]
        for c in s:
            if c != ']':
                st.append(c)
            else:
                string = ''
                while st:
                    top = st.pop()
                    if top == '[':
                        break
                    else:
                        string = top + string
                count,multiplier = 0,1
                while st and digit(st[-1]):
                    count += int(st.pop()) * multiplier
                    multiplier *= 10
                for _ in range(count):
                    st.append(string)
        return ''.join(st)



import unittest

class TestSolution(unittest.TestCase):
    def testDecodeString(self):
        s = Solution()
        self.assertEqual(s.decodeString(s = "3[a]2[bc]"), "aaabcbc")
        self.assertEqual(s.decodeString(s = "3[a2[c]]"), "accaccacc")
        self.assertEqual(s.decodeString(s = "2[abc]3[cd]ef"), "abcabccdcdcdef")
        self.assertEqual(s.decodeString(s = "11[leetcode]"), "leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode")


if __name__ == '__main__':
    unittest.main()