# Write any import statements here

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Write your code here
  if not C: return 0
  if X > Y: X,Y = Y,X
  A_index = [i for i in range(N) if C[i] == 'A']
  ans = 0
  for i in A_index:
    leftP = leftB = rightP = rightB = 0
    for j in range(X, Y + 1):
      left, right = i - j, i + j
      if left < 0 or right >= N:
        break
      leftP += 1 if C[left] == 'P' else 0
      leftB += 1 if C[left] == 'B' else 0
      rightP += 1 if C[right] == 'P' else 0
      rightB += 1 if C[right] == 'B' else 0
    ans += min(leftP, rightB)
    ans += min(leftB, rightP)
  return ans

def main():
  print(getArtisticPhotographCount(N=5, C='APABA', X=1, Y=2))
  print(getArtisticPhotographCount(N=5, C='APABA', X=2, Y=3))
  print(getArtisticPhotographCount(N=8, C='.PBAAP.B', X=1, Y=3))

if __name__ == '__main__':
  main()
