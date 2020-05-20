class Solve:
  n = d = 0

  def bsearch(self,l, r):
    if l > r:
      return 'NO'
    mid = (l+r) // 2
    xdiv =  self.d//(mid+1) + (1 if self.d%(mid+1) else 0) 
    if mid + xdiv <= self.n:
      return 'YES'
    elif mid >= xdiv:
      return self.bsearch(l,mid-1)
    else:
      return self.bsearch(mid+1,r)
    
  def solve(self):
    if self.d <= self.n:
      return 'YES'
    return self.bsearch(1, self.n)

def main():
  for _ in [0]*int(input()):
    s = Solve()
    s.n,s.d = map(int, input().split())
    print(s.solve())
  
main()
