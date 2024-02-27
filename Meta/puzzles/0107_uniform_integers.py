from typing import List
# Write any import statements here

def getUniformIntegerCountInInterval(A: int, B: int) -> int:
  # Write your code here

  def count(num):
    c,first = 0,0
    while num > 0:
      c += 1
      first = num if num < 10 else 0
      num //= 10
    return (c, first)
  
  def countLow():
    nonlocal ans
    for digit in range(lowFirst, 10):
      uniform = 0
      for _ in range(lowCount):
        uniform *= 10
        uniform += digit
      if uniform >= A:
        ans += 1

  def countHigh():
    nonlocal ans
    for digit in range(1, highFirst + 1):
      uniform = 0
      for _ in range(highCount):
        uniform *= 10
        uniform += digit
      if uniform <= B:
        ans += 1


  if A < 0 or B < 0: return -1
  lowCount,lowFirst = count(A)
  highCount,highFirst = count(B)
  ans = (highCount - lowCount - 1) * 9
  countLow()
  countHigh()
  return ans


def main():
  print(getUniformIntegerCountInInterval(A=75, B=300))
  print(getUniformIntegerCountInInterval(A=1, B=9))
  print(getUniformIntegerCountInInterval(A=999999999999, B=999999999999))

if __name__ == '__main__':
  main()
