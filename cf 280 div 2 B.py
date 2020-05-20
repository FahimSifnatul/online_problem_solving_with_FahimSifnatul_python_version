from sys import *

n,k = map(int,stdin.readline().split())
a = list(map(int,stdin.readline().split()))
a.sort()
mx = 1.0
for i in range(1,len(a)):
    mx = max( mx, a[i] - a[i-1] )
if a[0] == 0 and a[len(a)-1] != k:
    mx = max(mx, 2*(k - a[len(a)-1]) )
elif a[0] != 0 and a[len(a)-1] == k:
    mx = max(mx, 2*a[0] )
else:
    mx = max(mx, 2*a[0],2*(k-a[len(a)-1]))
stdout.write('%.10f' % (mx/2))
