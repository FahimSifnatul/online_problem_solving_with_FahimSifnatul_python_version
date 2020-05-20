from sys import stdin, stdout
n = int(stdin.readline())
half = list(map(int,stdin.readline().split()))
full = [0 for i in range(n)]
full[0] = 0
full[n-1] = half[0]
for i in range(1,n>>1):
    full[n-i-1] = min(full[n-i],half[i])
    if abs(full[n-i-1] - half[i]) >= full[i-1]:
        full[i] = abs(full[n-i-1] - half[i])
    else:
        full[i] = full[i-1]
        full[n-i-1] = half[i] - full[i]
stdout.write(' '.join(str(full[i]) for i in range(n)))
