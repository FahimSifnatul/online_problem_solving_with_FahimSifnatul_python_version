from sys import stdin,stdout
from math import sqrt
b = int(stdin.readline())
sq = int(sqrt(b + 1))
cnt = 0
for i in range(1,sq+1):
    if b%i == 0:
        if i*i == b:
            cnt += 1
        else:
            cnt += 2
stdout.write('%d' % cnt)
