from sys import stdin, stdout

def main():
  r = stdin.readline
  w = stdout.write
  for i in range(int(input())):
    n,k = map(int, r().split())
    half = k//2
    a1 = n//k + 1
    ans = a1*half
    ans = min(n, ans+(k-half)*(a1-1))
    w('%d\n' % ans)

main()
