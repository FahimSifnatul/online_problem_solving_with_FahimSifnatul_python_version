from sys import *

t = int(stdin.readline())
while t:
    t -= 1
    s,a,b,c = map(int,stdin.readline().split())
    stdout.write('%d\n' % (s//c + (s//c)//a*b)) 
