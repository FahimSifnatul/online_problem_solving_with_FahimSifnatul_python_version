from sys import stdin, stdout
from math import sqrt

class Solve:
  def sieve(self, prime, cnt):
    prime.append(2)
    cnt[2] = 0
    check = [1 for i in range(317)]
    for i in range(3, 317, 2):
      if check[i]:
        cnt[i] = 0
        prime.append(i) 
        for j in range(i+2*i, 317, 2*i):
          check[j] = 0
    return 0

  def __init__(self):
    R = stdin.readline
    W = stdout.write
    prime, cnt = [], {}
    self.sieve(prime, cnt)
    l = len(prime)
    n = int(input())
    a = [int(x) for x in R().split()]
    mx = 1
    for i in range(n):
      for j in range(l):
        if a[i]%prime[j] == 0:
          cnt[prime[j]] += 1
          mx = max(mx, cnt[prime[j]])
          while a[i]%prime[j] == 0:
            a[i] //= prime[j]
      if a[i] > 1:
        if a[i] not in cnt:
          cnt[a[i]] = 1;
        else:
          cnt[a[i]] += 1
          mx = max(mx, cnt[a[i]])
    W('%d\n' % mx)

def main():
  s = Solve()

main()




















