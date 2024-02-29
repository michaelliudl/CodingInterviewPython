import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def are_they_equal(array_a, array_b):
  # Write your code here
  if not array_a and not array_b:
    return True
  if not array_a or not array_b:
    return False
  if len(array_a) != len(array_b):
    return False
  n = len(array_a)
  map_a, map_b = {}, {}
  for i in range(n):
    map_a[array_a[i]] = map_a.get(array_a[i], 0) + 1
    map_b[array_b[i]] = map_b.get(array_b[i], 0) + 1
  if len(map_a) != len(map_b):
    return False
  for ka, va in map_a.items():
    if ka not in map_b or va != map_b[ka]:
      return False
  return True
  

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.
def printString(string):
  print('[\"', string, '\"]', sep='', end='')

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
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  n_1 = 4
  a_1 = [1, 2, 3, 4]
  b_1 = [1, 4, 3, 2]
  expected_1 = True
  output_1 = are_they_equal(a_1, b_1)
  check(expected_1, output_1)

  n_2 = 4
  a_2 = [1, 2, 3, 4]
  b_2 = [1, 2, 3, 5]  
  expected_2 = False
  output_2 = are_they_equal(a_2, b_2)
  check(expected_2, output_2)

  # Add your own test cases here
  