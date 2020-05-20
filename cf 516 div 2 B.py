from sys import stdin,stdout
stdout.write('\n'.join([str((1<<bin(int(stdin.readline())).count('1'))) for i in range(int(stdin.readline()))]))
