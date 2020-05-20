from sys import stdin, stdout
from math import ceil

class Solve:
  def __init__(self):
    R = stdin.readline
    W = stdout.write
    n, p, q, k = [int(x) for x in R().split()]
    a = [int(x) for x in R().split()]
    for i in range(n):
      tmp = a[i] % (p+q)
      a[i] = (tmp-p if tmp >= p else 0) if tmp else q
    a.sort()
    cnt = 0
    for i in range(n):
      if a[i] == 0:
        cnt += 1
      else:
        k -= ceil(a[i]/p)
        if k >= 0:
          cnt += 1
        else:
          break
    W('%d' % cnt)

def main():
  s = Solve()

main()
