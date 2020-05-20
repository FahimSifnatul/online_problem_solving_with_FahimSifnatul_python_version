ans = []
for i in [0]*int(input()):
  l = int(input())
  a, b, x, y, mis = input(), input(), set(), set(), 0
  for j in range(l):
    if a[j] != b[j]:
      x.add(a[j])
      y.add(b[j])
      mis += 1
  ans.append('no' if len(x)>1 or len(y)>1 or mis!=2 else 'yes')
print('\n'.join(ans))
