from typing import List
# Write any import statements here

def getMaxDamageDealt(N: int, H: List[int], D: List[int], B: int) -> float:
  # Write your code here
  if not H or not D: 0.0
  ans = 0
  for i in range(N - 1):
    for j in range(i + 1, N):
      damageIJ = (H[i] / B) * (D[i] + D[j]) + (H[j]/ B) * D[j]
      damageJI = (H[j] / B) * (D[i] + D[j]) + (H[i]/ B) * D[i]
      ans = max(ans, damageIJ, damageJI)
  return ans


def main():
  print(getMaxDamageDealt(N=3, H = [2, 1, 4], D = [3, 1, 2], B=4))
  print(getMaxDamageDealt(N=4, H = [1, 1, 2, 100], D = [1, 2, 1, 3], B=8))
  print(getMaxDamageDealt(N=4, H = [1, 1, 2, 3], D = [1, 2, 1, 100], B=8))

if __name__ == '__main__':
  main()
