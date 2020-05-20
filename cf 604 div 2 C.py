from sys import stdin, stdout
for i in range(int(input())):
  n = int(input())
  p = stdin.readline().split()
  if n < 6:
    stdout.write('0 0 0\n')
    continue
  himed = (n>>1)
