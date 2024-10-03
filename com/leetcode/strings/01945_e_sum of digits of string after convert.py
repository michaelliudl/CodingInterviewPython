from typing import List

class Solution:

    def getLucky(self, s: str, k: int) -> int:
        converted = []
        for char in s:
            converted.append(str(ord(char) - ord('a') + 1))
        res = int(''.join(converted))
        for _ in range(k):
            num = res
            res = 0
            while num > 0:
                res += num % 10
                num //= 10
            print(res)
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