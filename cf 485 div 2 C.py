from sys import stdin, stdout

class Solve:
  cnt = 0
  def DP(self, item_no, weight, font, cost, dp):
    self.cnt += 1
    if not item_no or not weight:
      return 0
    if dp[item_no][weight] != 0:
      return 0
    self.DP(item_no-1, weight, font, cost, dp)
    self.DP(item_no-1, weight-1, font, cost, dp)
    if weight <= 1:
      dp[item_no][weight] = min(dp[item_no-1][weight], cost[item_no])
    else:
      dp[item_no][weight] = min(dp[item_no-1][weight], dp[item_no-1][weight-1] + cost[item_no])
    
  def __init__(self):
    R = stdin.readline
    W = stdout.write
    n = int(input())
    font = [0] + [int(x) for x in R().split()]
    cost = [0] + [int(x) for x in R().split()]
    dp = [[0, 0, 0, 0] for i in range(n+1)]
    dp[1][1] = dp[1][2] = dp[1][3] = cost[1]
    dp[2][2] = dp[2][3] = cost[1] + cost[2]
    dp[3][3] = cost[1] + cost[2] + cost[3]
    self.DP(n, 3, font, cost, dp)
    for i in range(n+1):
      for j in range(4):
        W('%d ' % dp[i][j])
      print()
    print(self.cnt)

def main():
  s = Solve()

main()
























