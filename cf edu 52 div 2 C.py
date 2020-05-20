from sys import stdin,stdout
def main():
    n,k = map(int,stdin.readline().split())
    a = list(map(int,stdin.readline().split()))
    h_cnt = [0 for i in range(200005) ]
    mn,mx = 200000, 1
    for i in range(n):
        h_cnt[ a[i] ] += 1
        mx = max(mx,a[i])
    tmp = mx
    while tmp:
        if h_cnt[ tmp ] == n:
            break
        h_cnt [ tmp ] += h_cnt[ tmp + 1 ]
        tmp -= 1
    tmp = 0
    ans = 0
    while mx:
        if h_cnt[ mx ] == n:
            break
        if h_cnt[ mx ] + tmp > k:
            tmp = 0
            ans += 1
        else:
            tmp += h_cnt[ mx ]
            mx -= 1
    if tmp: 
        ans += 1
    stdout.write( '%d' % ans )
    
main()















