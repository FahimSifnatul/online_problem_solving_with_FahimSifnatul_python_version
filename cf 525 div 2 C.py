from sys import stdin, stdout

class Solve:
  def __init__(self):
    R = stdin.readline
    W = stdout.write
    n = int(input())
    a = [int(x)+100000 for x in R().split()]
    ans = [str(n+1), '1 ' + str(n) + ' 100000']
    for i in range(n):
      ans.append('2 ' + str(i+1) + ' ' + str(a[i]-i))
    W('\n'.join(ans))
    

def main():
  s = Solve()

main()
