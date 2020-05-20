from sys import stdin,stdout               
vis,x,y = [ [0 for j in range(1001)] for i in range(1001) ], [], []

def bfs(a,b,n):
    vis[a][b],q = 1, [ [a,b] ]
    while len(q):
        u = q[0]
        del q[0]
        for i in range(n):
            if not vis[x[i]][y[i]] and (x[i] == u[0] or y[i] == u[1]):
                vis[x[i]][y[i]] = 1
                q.append([x[i],y[i]])

def main():
    n = int(stdin.readline())
    cnt = 0
    for i in range(n):
        a,b = map(int,stdin.readline().split())
        x.append(a)
        y.append(b)
    for i in range(n):
        if not vis[x[i]][y[i]]:
            cnt += 1
            bfs(x[i],y[i],n)
    stdout.write('%d' % (cnt - 1))
   
main()    







