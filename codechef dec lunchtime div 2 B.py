from sys import stdin, stdout

def main():
  r = stdin.readline
  w = stdout.write
  for i in range(int(input())):
    n = int(input())
    a = [0] + [int(x) for x in r().split()]
    pos = dict()
    for i in range(1, n+1):
      pos[a[i]] = i
    a.sort()
    ans,j,joma = 0,pos[a[1]],a[1]
    for i in range(1, n+1):
      if pos[a[i]] <= j:
        ans += joma*pos[a[i]]
        j = pos[a[i]]
        if i > 1:
          joma = a[i] - joma
    w('%d\n' % ans)

main()
