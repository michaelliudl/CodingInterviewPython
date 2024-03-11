import math
# Add any extra import statements you may need here


# Add any helper functions you may need here
def search(arr, start, end, target):
  low, high, targetIndex = start, end, -1
  while low < high:
    mid = low + (high - low) // 2
    if arr[mid] == target:
      targetIndex = mid
      break
    elif arr[mid] > target:
      high = mid
    else:
      low = mid + 1
  count = 0
  if targetIndex > 0:
    count = 1
    for i in range(1, min(abs(targetIndex - start), abs(end - targetIndex))):
      if arr[targetIndex - i] != target and arr[targetIndex + i] != target:
        break
      if arr[targetIndex - i] == target:
        count += 1
      if arr[targetIndex + i] == target:
        count += 1
  return count


def countPairs(arr, k):
  # Write your code here
  if not arr:
    return 0
  n = len(arr)
  result = 0
  for i in range(n - 1):
    diff = k - arr[i]
    count = search(arr, i + 1, n, diff)
    result += count
  return result

def countPairsHash(arr, k):
  # Write your code here
  if not arr:
    return 0
  map = {}
  for index, num in enumerate(arr):
    if num not in map:
      map[num] = set()
    map[num].add(index)
  result = 0
  for num in arr:
    diff = k - num
    if num in map and diff in map:
      if num == diff:
        l = len(map[num])
        result += (l * (l - 1)) // 2
      else:
        result += len(map[num]) * len(map[diff])
        del map[diff]
      del map[num]
  return result












# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

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
    print(wrongTick, 'Test #', test_case_number, ': Expected ', expected, sep='', end='')
    print(' Your output: ', output, end='')
    print()
  test_case_number += 1

if __name__ == "__main__":
  output_1 = countPairs([1, 2, 3, 4, 5, 6, 7], 8)
  check(3, output_1)

  output_2 = countPairs([1, 2, 3, 4, 5, 6, 7], 98)
  check(0, output_2)

  # Add your own test cases here
  