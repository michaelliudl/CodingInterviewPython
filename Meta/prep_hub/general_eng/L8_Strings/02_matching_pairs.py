import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def matching_pairs(s, t):
  # Write your code here
  if not s or not t:
    return 0
  n = len(s)
  s_index_char, s_char_index, t_index_char, t_char_index = {}, {}, {}, {}
  ans = 0
  for i in range(n):
    if s[i] == t[i]:
      ans += 1
    else:
      s_index_char[i] = s[i]
      if s[i] not in s_char_index:
        s_char_index[s[i]] = set()
      s_char_index[s[i]].add(i)
      t_index_char[i] = t[i]
      if t[i] not in t_char_index:
        t_char_index[t[i]] = set()
      t_char_index[t[i]].add(i)
  if ans == n:
    for _, freq in s_char_index.items():
      if freq > 1:
        return n
    return n - 2
  for index_s, char_s in s_index_char.items():
    if char_s in t_char_index and t_index_char[index_s] in s_char_index:
      for index in t_char_index[char_s]:
        if index in s_char_index[t_index_char[index_s]]:
          return ans + 2
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
  s_1, t_1 = "abcde", "adcbe"
  expected_1 = 5
  output_1 = matching_pairs(s_1, t_1)
  check(expected_1, output_1)

  s_2, t_2 = "abcd", "abcd"
  expected_2 = 2
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)

  # Add your own test cases here
  