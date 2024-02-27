from typing import List

class Solution:

    def removeStars(self, s: str) -> str:
        if not s: return s
        arr = []
        for c in s: arr.append(c)
        left = 0
        for i in range(len(arr)):
            if arr[i] == '*':
                if left > 0:
                    left -= 1
            else:
                arr[left] = arr[i]
                left += 1
        return ''.join(arr[:left])

    def removeStarsStack(self, s: str) -> str:
        if not s: return s
        st=[]
        for c in s:
            if c=='*' and st:
                st.pop()
            else:
                st.append(c)
        return ''.join(st)


import unittest

class TestSolution(unittest.TestCase):
    pass



if __name__ == '__main__':
    unittest.main()