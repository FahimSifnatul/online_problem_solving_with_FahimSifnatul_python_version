from sys import stdin, stdout

def main():
  r = stdin.readline
  w = stdout.write
  for t in range(int(input())):
    n = int(input())
    a = [int(x) for x in r().split()]
    yasser, mx = sum(a), max(a)
    adel = mx
    cnt, flg = 0, 1
    for i in range(n):
      if cnt == 0:
        adel, cnt = a[i], 1
      else:
        adel += a[i]
        cnt += 1
        
      if adel <= 0:
        adel, cnt = mx, 0
      if cnt < n and adel >= yasser:
        flg = 0
        break
    w('%s\n' % ['NO', 'YES'][flg])

main()
