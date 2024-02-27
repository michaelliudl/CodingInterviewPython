from typing import List
# Write any import statements here

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
  # Write your code here
  if not R: return 0
  ans = 0
  for i in range(N-2, -1, -1):
    if R[i] >= R[i + 1]:
      R[i] = R[i + 1] - 1
      ans += 1
      if R[i] <= 0:
        return -1
  return ans

def main():
  print(getMinimumDeflatedDiscCount(N=5, R=[2, 5, 3, 6, 5]))
  print(getMinimumDeflatedDiscCount(N=3, R=[100, 100, 100]))
  print(getMinimumDeflatedDiscCount(N=4, R=[6, 5, 4, 3]))

if __name__ == '__main__':
  main()
