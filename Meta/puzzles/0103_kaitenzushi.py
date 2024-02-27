from typing import List,Deque
# Write any import statements here

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  # Write your code here
  if not D: return 0
  ans = 0
  typeQueue = Deque()
  typeMap = {}
  for type in D:
    if type not in typeMap:
      typeMap[type] = typeMap.get(type, 0) + 1
      typeQueue.append(type)
      ans += 1
    while len(typeQueue) > K:
      popped = typeQueue.popleft()
      typeMap[popped] -= 1
      if not typeMap[popped]:
        del typeMap[popped]
  return ans

def main():
  print(getMaximumEatenDishCount(N=6, D=[1, 2, 3, 3, 2, 1], K=1))
  print(getMaximumEatenDishCount(N=6, D=[1, 2, 3, 3, 2, 1], K=2))
  print(getMaximumEatenDishCount(N=7, D=[1, 2, 1, 2, 1, 2, 1], K=2))

if __name__ == '__main__':
  main()
