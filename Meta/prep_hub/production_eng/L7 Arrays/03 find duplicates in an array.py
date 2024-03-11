import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def findDuplicates(arr):
  # Write your code here
  if not arr:
    return arr
  n = len(arr)
  result = [0] * n
  for num in arr:
    result[num] += 1
  left = 0
  for i in range(n):
    if result[i] > 1:
      result[left] = i
      left += 1
  return result[:left]
  









# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, ' Test #', test_case_number, sep='')
  else:
    print(wrongTick, ' Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  test_1 = [0,3,1,2]
  expected_1 = []
  output_1 = findDuplicates(test_1)
  check(expected_1, output_1)
  
  test_2 = [2,3,1,2,3]
  expected_2 = [2,3]
  output_2 = findDuplicates(test_2)
  check(expected_2, output_2)

  # Add your own test cases here
  