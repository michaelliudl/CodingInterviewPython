import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def rotationalCipher(input_str, rotation_factor):
  # Write your code here
  if not input_str:
    return ""
  ans = [''] * len(input_str)
  for i,ch in enumerate(input_str):
    start = end = ''
    if 'A' <= ch <= 'Z':
      start = 'A'
      end = 'Z'
    elif 'a' <= ch <= 'z':
      start = 'a'
      end = 'z'
    elif '0' <= ch <= '9':
      start = '0'
      end = '9'
    if start and end:
      factor = rotation_factor % (ord(end) - ord(start) + 1)
      rotatedOrd = ord(ch) + factor
      if rotatedOrd > ord(end):
        rotatedOrd = ord(start) + (rotatedOrd - ord(end) - 1)
      ans[i] = chr(rotatedOrd)
    else:
      ans[i] = ch
  return ''.join(ans)
        
      











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
  input_1 = "All-convoYs-9-be:Alert1."
  rotation_factor_1 = 4
  expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
  output_1 = rotationalCipher(input_1, rotation_factor_1)
  check(expected_1, output_1)

  input_2 = "abcdZXYzxy-999.@"
  rotation_factor_2 = 200
  expected_2 = "stuvRPQrpq-999.@"
  output_2 = rotationalCipher(input_2, rotation_factor_2)
  check(expected_2, output_2)

  # Add your own test cases here
  