from sys import stdin, stdout

class Solve:
  def __init__(self):
    R = stdin.readline
    W = stdout.write
    ans = []
    for _ in range(int(input())):
      n = int(input())
      cnt = 0
      while n >= 10:
        cnt += n - n%10
        n = n%10 + n//10
      cnt += n
      ans.append(str(cnt))
    W('\n'.join(ans))

def main():
  s = Solve()

main()
