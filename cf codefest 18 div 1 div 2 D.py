from sys import stdin, stdout

def bfs(v, ch):
  q = [1]
  ans = [1]
  ch[1] = True
  while q:
    u = q[0]
    del q[0]
    for x in v[u]:
      if x not in ch:
        ch[x] = True
        q.append(x)
        ans.append(x)
  return ans
      

def main():
  r = stdin.readline
  w = stdout.write
  n = int(input())
  v, ch, order = dict(), dict(), dict()
  for i in range(n-1):
    x,y = map(int, r().split())
    if x not in v:
      v[x] = []
    if y not in v:
      v[y] = []
    v[x].append(y)
    v[y].append(x)
  seq = [int(x) for x in r().split()]
  if n == 1:
    w('yes')
    return 0
  for i in range(n):
    order[seq[i]] = i
  for i in range(1,n+1):
    v[i].sort(key = lambda x: order[x])
  ans = bfs(v, ch)
  w('yes' if seq == ans else 'no')

main()
	




















