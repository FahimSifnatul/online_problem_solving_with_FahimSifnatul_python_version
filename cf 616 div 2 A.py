from sys import stdin, stdout

class Solve:
  def __init__(self):
    R = stdin.readline
    W = stdout.write
    for _ in range(int(input())):
      n = int(input())
      s = R()
      ans, flg = '', 0
      for i in range(n):
        if int(s[i]) % 2 and flg < 2:
          ans += s[i]
          flg += 1
        if flg == 2:
          break
      if len(ans) == 2:
        W('%s\n' % ans)
      else:
        W('-1\n')

def main():
  s = Solve()

main()
