print('%s' % (lambda x,y,z,t1,t2,t3 : 'YES' if abs(z-x)*t2 + abs(x-y)*t2 + 3*t3 <= abs(x-y)*t1 else 'NO')(*map(int,input().split())))
