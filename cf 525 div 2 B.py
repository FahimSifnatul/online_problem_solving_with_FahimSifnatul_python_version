from sys import stdin,stdout
n,k = map(int,stdin.readline().split())
st = [0] + list(sorted(set(map(int,input().split()))))
stdout.write('\n'.join(['0' if i >= len(st) else str(st[i]-st[i-1]) for i in range(1,k+1)]))
    
