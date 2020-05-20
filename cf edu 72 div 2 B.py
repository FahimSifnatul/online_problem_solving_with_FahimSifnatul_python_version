from sys import stdin, stdout
from math import ceil

global mxd
class Val:
	def __init__(self, d, h, x):
		self.h = d - h
		self.x = x
		global mxd
		mxd = max(mxd, d)
	def __lt__(self, other):
		return self.h > other.h

ans = []		
for i in range(int(stdin.readline())):
	global mxd
	mxd = 0
	val = (lambda q,x : [(lambda d,h : Val(d,h,x))(*map(int, stdin.readline().split())) for j in range(q)])(*map(int,stdin.readline().split()))
	val.sort()
	ans.append('1' if val[0].x <= mxd else ('-1' if val[0].h <= 0 else str((val[0].x - mxd + val[0].h-1)//val[0].h + 1)))	
stdout.write('\n'.join(ans))
		
		
		
		
		
		
		
		
		
		
		
		
		
