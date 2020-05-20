from sys import stdin, stdout

class Solve:
  def tree_build(self, l, r, a):
    if l == r:
      return a[r]
    mn  = 10**6
    pos = 0
    for i in range(l, r+1):
      if a[i] < mn:
        mn  = a[i]
        pos = i
      
    if l < pos < r:
      return max(mn*(r-l+1), self.tree_build(l, pos-1, a), self.tree_build(pos+1, r, a))
    elif l == pos:
      return max(mn*(r-l+1), self.tree_build(pos+1, r, a))
    else:
      return max(mn*(r-l+1), self.tree_build(l, pos-1, a))  
    
  def __init__(self):
    R = stdin.readline
    W = stdout.write
    n = int(R())
    a = [int(x) for x in R().split()]
    ans = self.tree_build(0, n-1, a)
    W('%d\n' % ans)

def main():
  s = Solve()

main()
