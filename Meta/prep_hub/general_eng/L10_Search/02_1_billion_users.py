import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def getBillionUsersDay(growthRates):
  # Write your code here
  if not growthRates or max(growthRates) == 1:
    return -1
  prev, cur = 0, 1
  while True:
    total = sum([rate ** cur for rate in growthRates])
    if total >= 10 ** 9:
      break
    prev = cur
    cur *= 2
  while prev < cur:
    mid = prev + (cur - prev) // 2
    if sum([rate ** mid for rate in growthRates]) >= 10 ** 9:
      cur = mid
    else:
      prev = mid + 1
  return prev












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
  test_1 = [1.1, 1.2, 1.3]
  expected_1 = 79
  output_1 = getBillionUsersDay(test_1)
  check(expected_1, output_1)

  test_2 = [1.01, 1.02]
  expected_2 = 1047
  output_2 = getBillionUsersDay(test_2)
  check(expected_2, output_2)

  # Add your own test cases here
  