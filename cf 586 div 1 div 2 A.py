from sys import stdin, stdout
l = int(stdin.readline())
s = stdin.readline()
stdout.write(' '.join(['1' for i in range(s.count('n'))]+['0' for i in range(s.count('z'))]))
