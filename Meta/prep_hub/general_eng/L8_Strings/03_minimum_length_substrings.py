import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def min_length_substring(s, t):
  # Write your code here
  
  def is_substring(freq_s, freq_t):
    for ch, freq in freq_t.items():
      if ch not in freq_s or freq_s[ch] < freq:
        return False
    return True
  
  if not s:
    return 0
  if not t:
    return 1
  freq_t = {}
  for c in t:
    freq_t[c] = freq_t.get(c, 0) + 1
  freq_s = {}
  left = 0
  ans = float('inf')
  for right in range(len(s)):
    freq_s[s[right]] = freq_s.get(s[right], 0) + 1
    while is_substring(freq_s, freq_t):
      ans = min(ans, (right - left + 1))
      out = s[left]
      freq_s[out] -= 1
      left += 1
  return ans if ans != float('inf') else -1
  











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
  s1 = "dcbefebce"
  t1 = "fd"
  expected_1 = 5
  output_1 = min_length_substring(s1, t1)
  check(expected_1, output_1)

  s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
  t2 = "cbccfafebccdccebdd"
  expected_2 = -1
  output_2 = min_length_substring(s2, t2)
  check(expected_2, output_2)

  # Add your own test cases here
  