import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def numberOfWays(arr, k):
  # Write your code here
  
  def fact(n):
    result = 1
    for i in range(2, n + 1):
      result *= i
    return result
  
  def combi(n, r):
    if n == r:
      return 1
    n_fact = fact(n)
    r_fact = fact(r)
    n_minus_r_fact = fact(n - r)
    return n_fact // (r_fact * n_minus_r_fact)
  
  if not arr:
    return -1
  elem_idx = {}
  for i in range(len(arr)):
    if arr[i] not in elem_idx:
      elem_idx[arr[i]] = set()
    elem_idx[arr[i]].add(i)
  ans = 0
  used = set()
  for elem, idx in elem_idx.items():
    if elem in used:
      continue
    used.add(elem)
    diff = k - elem
    if elem == diff:
      ans += combi(len(idx), 2)
    elif diff in elem_idx and diff not in used:
      ans += len(idx) * len(elem_idx[diff])
      used.add(diff)
  return ans












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
  k_1 = 6
  arr_1 = [1, 2, 3, 4, 3]
  expected_1 = 2
  output_1 = numberOfWays(arr_1, k_1)
  check(expected_1, output_1)

  k_2 = 6
  arr_2 = [1, 5, 3, 3, 3]
  expected_2 = 4
  output_2 = numberOfWays(arr_2, k_2)
  check(expected_2, output_2)

  # Add your own test cases here
  