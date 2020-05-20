from sys import stdin,stdout
from bisect import *

def prev(val):
    cube[0] += val
    return cube[0]

n = int(stdin.readline())
cube = [0]
li = [(lambda i : prev((i*(i+1))//2))(i) for i in range(40) ]
#print(bisect(li,n,1,39))
stdout.write('%d' % (lambda x: x if li[x] == n else x-1)(bisect(li,n,1,39)))        

