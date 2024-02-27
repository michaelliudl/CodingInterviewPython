from typing import List
# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
  # Write your code here
  if not S: return 0
  one = two = 0
  for score in S:
    two = max(two, score // 2)
    one = max(one, score % 2)
  return one + two

def main():
  print(getMinProblemCount(N=6, S=[1, 2, 3, 4, 5, 6]))
  print(getMinProblemCount(N=4, S=[4, 3, 3, 4]))
  print(getMinProblemCount(N=4, S=[2, 4, 6, 8]))

if __name__ == '__main__':
  main()
