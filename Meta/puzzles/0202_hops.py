from typing import List
# Write any import statements here
import heapq

def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
  # Write your code here
  if not P: return 0
  pads = set(P)
  heapq.heapify(P)
  empty = [i for i in range(P[0], N + 1) if i not in pads]
  heapq.heapify(empty)
  ans = 0
  while P:
    ans += 1
    cur = heapq.heappop(P)
    next = cur + 1
    if next == N or empty[0] == N:
      continue
    if next == empty[0]:
      heapq.heappop(empty)
    heapq.heappush(P, next)
  return ans


def main():
  print(getSecondsRequired(N=6, F=3, P=[5,2,4]))
  print(getSecondsRequired(N=3, F=1, P=[1]))

if __name__ == '__main__':
  main()
