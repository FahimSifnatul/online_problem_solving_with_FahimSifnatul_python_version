from sys import stdin, stdout

class Solve:
  g = k = 0
  ans = []

  def bsearch(self, l, r, p, q):
    if l > r:
      return 0
    mid = (l+r) // 2
    tmp = self.g - q*mid
    if tmp < 0:
      return self.bsearch(l, mid-1, p, q)
    rem = tmp % p
    if not rem:
      self.ans.append(str(tmp // p))
      self.ans.append(' ')
      self.ans.append(str(mid))
      self.ans.append('\n')
      return 0
    if 2*rem >= p:
      return self.bsearch(l, mid-1, p, q)
    else:
      return self.bsearch(mid+1, r, p, q)
    
  def solve(self):
    r = stdin.readline
    w = stdout.write
    r = 2**63 - 1
    for t in range(int(input())):
      self.g, self.k = map(int, input().split())
      q = self.g // self.k + (1 if self.g%self.k else 0)
      p = self.g // self.k
      if p == 0:
        self.ans.append('0')
        self.ans.append(' ')
        self.ans.append(str(self.g//q))
        self.ans.append('\n')
      else:
        self.bsearch(0, p, p, q)
    w(''.join(self.ans))
    

def main():
  s = Solve()
  s.solve()

main()

















