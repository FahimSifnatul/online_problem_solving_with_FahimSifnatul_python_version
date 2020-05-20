from sys import stdin, stdout
stdout.write('\n'.join([(lambda a, b: 'yes' if a-b > 1 else 'no')(*map(int, stdin.readline().split())) for i in range(int(input()))]))
