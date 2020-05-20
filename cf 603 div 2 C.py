from math import sqrt
from sys import stdin, stdout
for i in range(int(input())):
  n = int(input())
  s,j,l = set([0,1]), 2, sqrt(n)
  while j <= l:
    s.add(j)
    s.add(int(n//j))
    j += 1
  s.add(n)
  a,l = sorted(s), len(s)
  stdout.write('%d\n' % l)
  for j in range(l):
    stdout.write('%d ' % a[j])
  stdout.write('\n')
