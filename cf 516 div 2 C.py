from sys import stdin,stdout
n = stdin.readline()
stdout.write(''.join((lambda s : sorted(s))(list(stdin.readline()))))
