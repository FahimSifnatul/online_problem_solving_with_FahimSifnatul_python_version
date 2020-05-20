from sys import stdin, stdout
from math import sqrt
ans = []
for i in range(int(input())):
  a, b, c = [int(x) for x in stdin.readline().split()]
  s = (a + b + c) / 2
  ans.append('Area = ' + '%.3f' % sqrt(s*(s-a)*(s-b)*(s-c)) if (a+b>c and b+c>a and c+a>b) else '0.000')
  ans.append('\n')
stdout.write(''.join(ans))
