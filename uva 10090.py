from sys import stdin, stdout

class Solve:
  n = c1 = n1 = c2 = n2 = x = y = gcd = 0
  ans = []

  def egcd(self, a, b):
    if b == 0:
      return [a, 1, 0]
    gcd, x, y = self.egcd(b, a%b)
    return [gcd, y, x - (a//b) * y]
    
  def __init__(self):
    R = stdin.readline
    W = stdout.write
    while True:
      self.n = int(input())
      if self.n == 0:
        break
      self.c1, self.n1 = [int(x) for x in R().split()]
      self.c2, self.n2 = [int(x) for x in R().split()]
      self.gcd, self.x, self.y = egcd(self.n1, self.n2)
      if self.n % self.gcd:
        self.ans += ['failed', '\n']
        continue
      
      
    #W(''.join(self.ans))

def main():
  s = Solve()

main()






































