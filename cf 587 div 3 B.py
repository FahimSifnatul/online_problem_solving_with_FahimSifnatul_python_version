n = int(input())
temp, a, cnt = list(map(int, input().split())), [], 0
for i in range(n):
	a.append((temp[i],i+1))
a.sort(reverse = True)
temp = []
for i in range(n):
	cnt += a[i][0] * i + 1
	temp.append(a[i][1])
print(cnt)
print(*temp)
