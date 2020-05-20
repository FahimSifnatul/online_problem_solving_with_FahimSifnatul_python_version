from sys import stdin, stdout

def bsearch(s, i, f, l, r, tmp):
    if l > r:
        return str(tmp)
    mid = ((l+r) >> 1)
    if s + mid > i + (f - mid):
        tmp = max(tmp, f - mid + 1)
        return bsearch(s, i, f, l, mid-1, tmp)
    else:
        return bsearch(s, i, f, mid+1, r, tmp)

stdout.write('\n'.join([(lambda s,i,f : bsearch(s,i,f,0,f,0))(*map(int, stdin.readline().split())) for i in range(int(stdin.readline()))]))
