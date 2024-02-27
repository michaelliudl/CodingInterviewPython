from typing import List
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  # Write your code here
  if not C: return 0
  prev,ans = 1,0
  for code in C:
    ans += min(abs(code - prev), (N + min(code, prev) - max(code, prev)))
    prev = code
  return ans

def main():
  print(getMinCodeEntryTime(N=3, M=3, C=[1, 2, 3]))
  print(getMinCodeEntryTime(N=10, M=4, C=[9, 4, 4, 8]))

if __name__ == '__main__':
  main()
