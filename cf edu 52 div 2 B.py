a = list( map(int,input().split()) )
print('%d' % ( (lambda v,e : 0 if v <= 2*e else v - 2*e)(*a) ) ,end = ' ')
if a[1] == 0:
    print(a[0])
else :
    ans = 0
    l = 1
    r = 100000
    while True:
        if l > r:
            break
        mid = (l+r)//2
        if mid*mid - mid - (a[1]<<1) >= 0:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    print( a[0] - ans)       
