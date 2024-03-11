import math
# Add any extra import statements you may need here
import heapq

# Add any helper functions you may need here

# Forward is easier
def findMaxProduct(arr):
  # Write your code here
  if not arr:
    return arr
  result = [-1] * len(arr)
  heap = []
  for index, num in enumerate(arr):
    heapq.heappush(heap, -num)
    if index > 1:
      prod = 1
      temp = [-1] * 3
      for i in range(3):
        value = heapq.heappop(heap)
        temp[i] = value
        prod *= -value
      result[index] = prod
      for value in temp:
        heapq.heappush(heap, value)
  return result

def findMaxProductBackward(arr):
  # Write your code here
  if not arr:
    return arr
  result = [-1] * len(arr)
  heap = []
  for index, num in enumerate(arr):
    heapq.heappush(heap, (-num, index))
  for i in range(len(arr) - 1, 1, -1):
    prod = 1
    temp = [None] * 3
    for j in range(3):
      while heap:
        value, index = heapq.heappop(heap)
        if index > i:
            continue
        else:
            prod *= -value
            temp[j] = (value, index)
            break
    result[i] = prod
    for value, index in temp:
      if index < i:
        heapq.heappush(heap, (value, index))
  return result

  









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
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  arr_1 = [1, 2, 3, 4, 5]
  expected_1 = [-1, -1, 6, 24, 60]
  output_1 = findMaxProduct(arr_1)
  check(expected_1, output_1)

  arr_2 = [2, 4, 7, 1, 5, 3]
  expected_2 = [-1, -1, 56, 56, 140, 140]
  output_2 = findMaxProduct(arr_2)
  check(expected_2, output_2)


  # Add your own test cases here
  