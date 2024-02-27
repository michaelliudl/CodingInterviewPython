from typing import List
# Write any import statements here

def getMaxVisitableWebpages(N: int, L: List[int]) -> int:
  # Write your code here

  def dfs(start, visited, steps):
    if start in visited:
      return steps
    visited.add(start)
    # if depth[start] > 0:
    #   return steps + depth[start]
    return dfs(L[start - 1], visited, steps + 1)

  if not L: return 0
  depth = [0] * (N + 1)
  ans = 0
  for i in range(N):
    visited = set()
    start = i + 1
    dep = dfs(start, visited, steps=0)
    # depth[start] = dep
    ans = max(ans, dep)
  # return max(depth)
  return ans

def main():
  print(getMaxVisitableWebpages(N=4, L = [4, 1, 2, 1]))
  print(getMaxVisitableWebpages(N=5, L = [4, 3, 5, 1, 2]))
  print(getMaxVisitableWebpages(N=5, L = [2, 4, 2, 2, 3]))

if __name__ == '__main__':
  main()
