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
    pass



if __name__ == '__main__':
    unittest.main()