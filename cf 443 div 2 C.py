from sys import stdin, stdout

class Solve:
  def __init__(self):
    R = stdin.readline
    W = stdout.write
    n = int(input())
    z, o = 0, 1023
    for i in range(n):
      op, x = R().split()
      x = int(x)
      if op == '|':
        z |= x
        o |= x
      elif op == '&':
        z &= x
        o &= x
      elif op == '^':
        z ^= x
        o ^= x
    ans = {'^' : 0, '|' : 0, '&' : 1023}
    for b in range(10):
      bit = 1 << b
      bitz = z & bit
      bito = o & bit
      if bool(bitz) and not bool(bito):
        ans['^'] |= bit
      elif bool(bitz) and bool(bito):
        ans['|'] |= bit
      elif not bool(bitz) and not bool(bito):
        ans['&'] ^= bit
    W('3\n')
    for op in ans:
      print(op, ans[op])

def main():
  s = Solve()
main()
























