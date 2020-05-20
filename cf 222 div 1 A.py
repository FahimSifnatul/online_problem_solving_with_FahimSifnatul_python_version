from sys import stdin,stdout
#from collections import deque
ok = lambda tx,ty,n,m : tx >=0 and tx < n and ty >= 0 and ty < m
dx = [1,-1,0,0]
dy = [0,0,1,-1]

class G:
    def __init__(self,a,b):
        self.x = a
        self.y = b

def bfs(x,y,adlist,vis,nodes,k,n,m):
    q = []
    adlist[x][y] = 'X' if nodes <= k else adlist[x][y]
    nodes,vis[x][y], l = nodes - 1, 1, 1
    q.append(G(x,y))
    while l:
        u = q[0]
        del q[0]
        l -= 1
        for i in range(4):
            tx,ty = dx[i] + u.x, dy[i] + u.y
            if ok(tx,ty,n,m):
                if vis[tx][ty] == 0 and adlist[tx][ty] == '.':
                    adlist[tx][ty] = 'X' if nodes <= k else adlist[tx][ty]
                    nodes,vis[tx][ty],l = nodes - 1, 1, l + 1
                    q.append(G(tx,ty))
    for i in range(n):
        stdout.write(''.join(adlist[i]))
                        
def main():
    n,m,k = map(int,stdin.readline().split())
    adlist = [list(stdin.readline()) for i in range(n) ]
    vis = [ [0 for j in range(m)] for i in range(n) ]
    nodes,x,y = 0,0,0
    for i in range(n):
        for j in range(m):
            if adlist[i][j] == '.':
                nodes,x,y = nodes + 1, i, j
    bfs(x,y,adlist,vis,nodes,k,n,m)         
    
main()     













