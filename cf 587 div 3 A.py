from sys import stdin, stdout

n, s, cnt = int(stdin.readline()), list(stdin.readline()), 0
for i in range(1, n, 2):
	s[i], cnt = (('a',cnt+1) if s[i] == 'b' else ('b',cnt+1)) if (s[i] == s[i-1]) else (s[i], cnt)
stdout.write(''.join([str(cnt)+'\n'] + s))
