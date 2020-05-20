def sieve(prime):
    ok = [0 for i in range(5005)]
    for i in range(3,100,2):
        if not ok[i>>1]:
            for j in range(i*i,10000,2*i):
                ok[j>>1] = 1;
    for i in range(1001,10000,2):
        if not ok[i>>1]:
            prime.append(str(i))

def adjacencylist(adlist):
    for i in range(1061):
        for j in range(1061):
            if prime[j][0] != prime[i][0] and prime[j][1] == prime[i][1] and prime[j][2] == prime[i][2] and  prime[j][3] == prime[i][3]:
                adlist[int(prime[i])].append(int(prime[j]))
            elif prime[j][0] == prime[i][0] and prime[j][1] != prime[i][1] and prime[j][2] == prime[i][2] and  prime[j][3] == prime[i][3]:
                adlist[int(prime[i])].append(int(prime[j]))
            elif prime[j][0] == prime[i][0] and prime[j][1] == prime[i][1] and prime[j][2] != prime[i][2] and  prime[j][3] == prime[i][3]:
                adlist[int(prime[i])].append(int(prime[j]))
            elif prime[j][0] == prime[i][0] and prime[j][1] == prime[i][1] and prime[j][2] == prime[i][2] and  prime[j][3] != prime[i][3]:
                adlist[int(prime[i])].append(int(prime[j]))

def bfs(src,des):
    cnt = 0
    dis = [-1 for i in range(5005)]
    dis[src>>1] = 0
    if src == des:
        print(0)
        return 0
    q = [src]
    while len(q) > 0:
        u = q[0]
        del q[0]
        l = len(adlist[u])
        for i in range(1,l):
            if dis[adlist[u][i]>>1] == -1:
                dis[adlist[u][i]>>1] = dis[u>>1] + 1
                q.append(adlist[u][i])
            if adlist[u][i] == des:
                print ( dis[adlist[u][i]>>1] )
                return 0
    print('Impossible')
    return 0


prime = []
sieve(prime)
adlist = [ [0] for i in range(10005) ]
adjacencylist(adlist)
t = int(input())
while t:
    src,des = map(int,input().split());
    bfs(src,des)
    t -= 1





























