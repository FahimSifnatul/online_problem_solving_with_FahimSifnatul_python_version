n,m = int(input()), int(input())
a,i = [int(input()) for i in range(n)], 0
a.sort()
mx,mn = a[len(a)-1] + m , a[len(a)-1]
while m > 0 and i < len(a):
    m,i = m-(mn - a[i]), i + 1
while m > 0:
    m,mn = m - len(a), mn + 1
print(mn,mx)    
