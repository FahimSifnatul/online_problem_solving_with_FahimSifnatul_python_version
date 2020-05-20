from bisect import bisect_left
ans = []
for i in range(int(input())):
  n = int(input())
  a = sorted([int(x) for x in input().split()])
  tmp = a[n-1]
  while tmp > 1:
    if n-bisect_left(a,tmp) >= tmp:
      break
    tmp -= 1
  ans.append(str(tmp))
print('\n'.join(ans))
