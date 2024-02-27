from typing import List
# Write any import statements here

def getSecondsRequired(R: int, C: int, G: List[List[str]]) -> int:
  # Write your code here

  def scan():
    startX,startY,portals = -1,-1,{}
    for i in range(R):
      for j in range(C):
        cur = G[i][j]
        if cur == 'S':
          startX,startY = i,j
        elif 'a' <= cur <= 'z':
          if cur not in portals:
            portals[cur] = set()
          portals[cur].add((i,j))
    return startX, startY, portals
  
  def valid(x, y):
    return 0 <= x < R and 0 <= y < C and G[x][y] != '#'
  
  dirs = [(-1,0), (1,0), (0,-1), (0,1)]
  
  def dfs(x, y, steps):
    nonlocal ans
    cur = G[x][y]
    if cur == 'E':
      ans = min(ans, steps)
      return
    visisted[x][y] = True
    if 'a' <= cur <= 'z':
      for nx, ny in portals[cur]:
        if not visisted[nx][ny]:
          dfs(nx, ny, steps + 1)
    for dx, dy in dirs:
      nx, ny = x + dx, y + dy
      if valid(nx, ny) and not visisted[nx][ny]:
        dfs(nx, ny, steps + 1)

  if not G: return -1
  startX,startY,portals = scan()
  ans = float('inf')
  visisted = [[False] * C for _ in range(R)]
  dfs(startX, startY, steps=0)
  return -1 if ans == float('inf') else ans

def main():
  print(getSecondsRequired(R=3, C=4, G=[[c for c in 'aS.b'],
                                        [c for c in '####'],
                                        [c for c in 'Eb.a']]))
  print(getSecondsRequired(R=3, C=3, G=[[c for c in '.E.'],
                                        [c for c in '.#E'],
                                        [c for c in '.S#']]))
  print(getSecondsRequired(R=3, C=4, G=[[c for c in 'a.Sa'],
                                        [c for c in '####'],
                                        [c for c in 'Eb.b']]))
  print(getSecondsRequired(R=1, C=9, G=[[c for c in 'xS..x..Ex']]))

if __name__ == '__main__':
  main()
