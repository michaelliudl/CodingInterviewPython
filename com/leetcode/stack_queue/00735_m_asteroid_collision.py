from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        def collision(ast, top):
            return ast < 0 and top > 0

        if not asteroids: return asteroids
        st = []
        for ast in asteroids:
            destroyed = False
            while st and collision(ast, st[-1]):
                if abs(ast) == abs(st[-1]):
                    st.pop()
                    destroyed = True
                    break
                elif abs(ast) > abs(st[-1]):
                    st.pop()
                else:
                    destroyed = True
                    break
            if not destroyed:
                st.append(ast)
        return st


import unittest

class TestSolution(unittest.TestCase):
    def testMinStack(self):
        s = MinStack()
        s.push(-2)
        s.push(0)
        s.push(-3)
        self.assertEqual(s.getMin(), -3)
        s.pop()
        self.assertEqual(s.top(), 0)
        self.assertEqual(s.getMin(), -2)
        s.pop()
        s.pop()
        self.assertEqual(s.getMin(), float('inf'))

    def testMinStack_1(self):
        s = MinStack()
        s.push(2)
        s.push(0)
        s.push(3)
        s.push(0)
        self.assertEqual(s.getMin(), 0)
        s.pop()
        self.assertEqual(s.getMin(), 0)
        s.pop()
        self.assertEqual(s.getMin(), 0)
        s.pop()
        self.assertEqual(s.getMin(), 2)



if __name__ == '__main__':
    unittest.main()