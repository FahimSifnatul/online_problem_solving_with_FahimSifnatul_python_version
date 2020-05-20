n,cnt = int(input()), 0
cross = [ input() for i in range(n) ]
for i in range(1,n-1):
    for j in range(1,n-1):
        if cross[i][j] == cross[i+1][j+1] == cross[i-1][j+1] == cross[i+1][j-1] == cross[i-1][j-1] == 'X':
            cnt += 1
print(cnt)
