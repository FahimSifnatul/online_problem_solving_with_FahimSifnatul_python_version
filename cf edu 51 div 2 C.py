from sys import stdin, stdout

class Solve:
  def __init__(self):
    R = stdin.readline
    W = stdout.write
    n = int(input())
    a = [int(x) for x in R().split()]
    ans = ['A' for i in range(n)]
    check = {}
    auniq = buniq = 0
    for i in range(n):
      if a[i] not in check:
        check[a[i]] = 0
      check[a[i]] += 1
      if check[a[i]] == 1:
        auniq += 1
      elif check[a[i]] == 2:
        auniq -= 1
    for i in range(n):
      if auniq == buniq:
        W('YES\n')
        W(''.join(ans))
        return
      if check[a[i]] == 1 and auniq > buniq+1:
        check[a[i]] = 0 
        ans[i] = 'B'
        auniq -= 1
        buniq += 1
    for i in range(n):
      if auniq == buniq:
        W('YES\n')
        W(''.join(ans))
        return
      if check[a[i]] > 2:
        check[a[i]] = 2 
        ans[i] = 'B'
        buniq += 1
    W('NO\n')

def main():
  s = Solve()

main()

















