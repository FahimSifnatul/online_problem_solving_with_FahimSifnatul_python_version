from sys import stdin,stdout
n = int(stdin.readline())
a = list(map(int,stdin.readline().split()))
a.insert(0,0)
k, step = 0, set()
for i in range(n):
    a[i] = a[i+1] - a[i]
for i in range(n):
    k, tmp, flg = k + 1, 0, 1
    for j in range(i+1,n):
        if a[j] != a[tmp]:
            flg = 0
            break
        tmp += 1
        if tmp == k:
            tmp = 0 
    if flg:
        for i in range(n):
            if not (i+1)%k:
                step.add(i+1)
stdout.write('%d\n' % len(step) )
step = sorted(step)
for i in range(len(step)):
    stdout.write('%d ' % step[i])
        








    
