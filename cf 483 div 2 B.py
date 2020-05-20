ok = lambda tx,ty : tx >= 0 and tx < n and ty >= 0 and ty < m  

def check(mine):
     for i in range(n):
         for j in range(m):
             dot = 0
             star = 0
             for k in range(8):
                 tx = i + dx[k]
                 ty = j + dy[k]
                 if ok( tx , ty ):
                     if mine[tx][ty] == '.':
                         dot += 1
                     elif mine[tx][ty] == '*':
                         star += 1
             if mine[i][j] == '*':
                 if dot > 0:
                     print( 'NO' )
                     return 0
             elif mine[i][j] == '.':
                 if star > 0:
                     print( 'NO' )
                     return 0
             else:
                 if int(mine[i][j]) != star:
                     print( 'NO' )
                     return 0
     print( 'YES' )                
    
dx = (1,-1,0,0,1,-1,1,-1)
dy = (0,0,1,-1,1,-1,-1,1)
n,m = map(int,input().split(' '))
mine = []
for i in range(n):
    mine.append(input())
check(mine)   





