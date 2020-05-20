from sys import stdout, stdin
ans = []
for i in range(int(input())):
	n = int(input())
	a = sorted(list(map(int, stdin.readline().split())))
	while True:
		if len(a) == 1 or a[0] == 2048:
			break
		elif a[0] == a[1]:
			a[1] += a[0]
		del a[0]
		a.sort()
	ans.append('yes' if a[0] == 2048 else 'no')
stdout.write('\n'.join(ans))
