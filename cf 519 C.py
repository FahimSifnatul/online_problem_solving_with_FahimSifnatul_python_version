from sys import stdin,stdout
a = list(input())
b = sorted(a)
l = len(a)
ans = ['0' for i in range(l)]
for i in range(1,l):
    if a == b:
        break
    if a[0] == 'a':
        if a[i] == 'a':
            a[0:i-1] = a[i-1:0:-1]
            ans[i-1] = '1'
    else:
        if a[i] == 'b':
            a[0:i-1] = a[i-1:0:-1]
            ans[i-1] = '1'
if a[0] == 'b':
    ans[l-1] = '1'
stdout.write(' '.join(ans))
    
