from sys import stdin
n = int(input())
a = [int(x) for x in stdin.readline().split()]
l = [1 for i in range(n)]
r = [1 for i in range(n)]
ans = 1
for i in range(1,n):
  if a[i-1] < a[i]:
    l[i] += l[i-1]
  ans = max(ans, l[i])
for i in range(n-2,-1,-1):
  if a[i] < a[i+1]:
    r[i] += r[i+1]
for i in range(1,n-1):
  if a[i-1] < a[i+1]:
    ans = max(ans, l[i-1]+r[i+1])
print(ans)

