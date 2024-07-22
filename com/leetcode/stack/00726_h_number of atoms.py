from typing import List, DefaultDict

class Solution:

    # Use stack of maps to track element:count for nested parens
    def countOfAtoms(self, formula: str) -> str:
        stack = [DefaultDict(int)]      # Init with empty map to collect final result
        index, n = 0, len(formula)
        while index < n:
            if formula[index] == '(':   # Init next level
                stack.append(DefaultDict(int))
                index += 1
            elif formula[index] == ')': # Closing parens, pop nested map and multiply potential count after it, merge result map with top of stack
                index += 1
                numStart = index
                while index < n and formula[index].isdigit():
                    index += 1
                count = 1 if numStart == index else int(formula[numStart:index])    # Count of nested elements
                curMap = stack.pop()
                prevMap = stack[-1]
                for k, v in curMap.items():         # Add current nested count to prev map
                    prevMap[k] += (v * count)
            else:                       # Check element and count, element starts with upper case letter and potetially followed by lower case letter 
                elemStart = index       # Element always start with upper case letter
                index += 1
                while index < n and formula[index].islower():
                    index += 1
                element = formula[elemStart:index]
                numStart = index
                while index < n and formula[index].isdigit():   # count is 1 if no number following element
                    index += 1
                count = 1 if numStart == index else int(formula[numStart:index])
                stack[-1][element] += count
        res = []
        elements = stack.pop()
        for elem in sorted(elements.keys()):
            res.append(elem)
            if elements[elem] > 1:
                res.append((str(elements[elem])))
        return ''.join(res)

import unittest

class TestSolution(unittest.TestCase):
    def testCountOfAtoms(self):
        s = Solution()
        self.assertEqual(s.countOfAtoms(formula = "H2O"), "H2O")
        self.assertEqual(s.countOfAtoms(formula = "Mg(OH)2"), "H2MgO2")
        self.assertEqual(s.countOfAtoms(formula = "K4(ON(SO3)2)2"), "K4N2O14S4")


if __name__ == '__main__':
    unittest.main()