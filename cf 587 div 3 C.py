from sys import stdin, stdout
from math import gcd

n, swords = int(input()), list(map(int,stdin.readline().split()))

swords.sort(reverse = True)
y, z, tmp = 0, 0, 0

for i in range(1,n):
	tmp = swords[0] - swords[i]
	y += tmp
	z = gcd(z, tmp)

stdout.write('%d %d' % (y//z,z))
