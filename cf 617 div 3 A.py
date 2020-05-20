from sys import stdin, stdout

class Solve:
  def __init__(self):
    R = stdin.readline
    W = stdout.write
    ans = []
    for _ in range(int(input())):
      n = int(input())
      a = [int(x) for x in R().split()]
      odd, even = 0, 0
      for i in range(n):
        if a[i]%2:
          odd += 1
        else:
          even += 1
      if odd == 0 or (odd%2 == 0 and even == 0):
        ans.append('NO\n')
      else:
        ans.append('YES\n')
    W(''.join(ans))
      

def main():
  s = Solve()

main()
