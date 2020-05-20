from sys import stdin,stdout
def ans(mx,l):
    for i in range(len(l)):
        if l[i] > mx + 1:
            return i+1
        mx = max(mx,l[i])
    return -1
n = int(stdin.readline())
l = list(map(int,stdin.readline().split()))
stdout.write('%d' % ans(-1,l))
