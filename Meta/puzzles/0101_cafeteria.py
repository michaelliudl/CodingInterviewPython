from typing import List
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  # Write your code here
  if not S: return 0
  S.sort()
  ans,left = 0,(1 - (K + 1))       # Add K virtual elements at begining
  for s in S:
    ans += (s - 1 - left - K) // (K + 1)
    left = s
  ans += ((N + K + 1) - 1 - left - K) // (K + 1)    # Add K virtual elemnent at end
  return ans

def main():
  print(getMaxAdditionalDinersCount(N=10, K=1, M=2, S=[2,6]))
  print(getMaxAdditionalDinersCount(N=15, K=2, M=3, S=[11,6,14]))

if __name__ == '__main__':
  main()
