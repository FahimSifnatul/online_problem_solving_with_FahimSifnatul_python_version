from sys import stdin, stdout
import os

class Val():
  mx = carry = 0

class Solve:
  def update(self, a, b, add, l, r, node, tree):
    
    if tree[node].carry != 0:
      tree[node].mx += tree[node].carry
      if l != r:
        tree[2*node+1].carry += tree[node].carry
        tree[2*node+2].carry += tree[node].carry
      tree[node].carry = 0
      
    if r < a or l > b:
      return 0;
    
    if a <= l <= r <= b:
      tree[node].mx += add
      if l != r:
        tree[2*node+1].carry += add
        tree[2*node+2].carry += add
      return 0
    
    mid = (l+r) // 2
    self.update(a, b, add, l, mid, 2*node+1, tree)
    self.update(a, b, add, mid+1, r, 2*node+2, tree)
    tree[node].mx = max(tree[node].mx, tree[2*node+1].mx, tree[2*node+2].mx)
    
  def __init__(self):
    R = stdin.readline
    W = stdout.write
    #f = open(os.environ['OUTPUT_PATH'], 'w')
    
    n, q = [int(x) for x in R().split()]
    tree = [Val() for i in range(10000000)]
    for _ in range(q):
      a, b, add = [int(x) for x in R().split()]
      self.update(a-1, b-1, add, 0, n-1, 0, tree)

    #f.write(str(tree[0].mx) + '\n')
    #f.close()
    #print(tree[0].mx)

def main():
  s = Solve()

main()


















