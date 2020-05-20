from sys import stdin, stdout

class Solve:
  def __init__(self):
    r = stdin.readline
    w = stdout.write
    ans = []
    for _ in range(int(input())):
      n = int(r())
      two, power = 3, 2
      while n%two:
        two   += 2**power
        power += 1
      ans.append(str(n//two))
    w('\n'.join(ans))

def main():
  s = Solve()

main()
