from sys import stdin
for i in range(int(input())):
  r,sec = map(int, stdin.readline().split())
  a,j = [0 for i in range(r)], 0
  while sec:
    a[j] += 1
    sec -= 1
    j += 1
    if j == r:
      j = 0
  ans = 0
  for j in range(r):
    ans += a[j]**2
  print(ans)
