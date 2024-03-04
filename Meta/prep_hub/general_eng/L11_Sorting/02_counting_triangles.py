import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def countDistinctTriangles(arr):
  # Write your code here
  if not arr:
    return 0
  sides = set()
  for side1, side2, side3 in arr:
    sideMap = {}
    sideMap[side1] = sideMap.get(side1, 0) + 1
    sideMap[side2] = sideMap.get(side2, 0) + 1
    sideMap[side3] = sideMap.get(side3, 0) + 1
    sides.add(tuple(sorted([(side, count) for side, count in sideMap.items()])))
  return len(sides)




# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  arr_1 = [(7, 6, 5), (5, 7, 6), (8, 2, 9), (2, 3, 4), (2, 4, 3)]
  expected_1 = 3
  output_1 = countDistinctTriangles(arr_1)
  check(expected_1, output_1)

  arr_2 = [(3, 4, 5), (8, 8, 9), (7, 7, 7)]
  expected_2 = 3
  output_2 = countDistinctTriangles(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
  