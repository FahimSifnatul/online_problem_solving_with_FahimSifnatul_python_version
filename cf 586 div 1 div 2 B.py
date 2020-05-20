from sys import stdin, stdout
from math import sqrt

n = int(stdin.readline())
a = []
for i in range(n):
    a.append(list(map(int,stdin.readline().split())))
for i in range(n):
    if i > 0 and i < n-1:
        stdout.write('%d ' % (int(sqrt((a[i-1][i]*a[i][i+1])/a[i-1][i+1]))))
    elif i == 0:
        stdout.write('%d ' % (int(sqrt((a[n-1][i]*a[i][i+1])/a[n-1][i+1]))))
    else:
        stdout.write('%d ' % (int(sqrt((a[i-1][i]*a[i][0])/a[i-1][0]))))


        
