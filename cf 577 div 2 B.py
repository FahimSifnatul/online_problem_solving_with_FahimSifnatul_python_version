from sys import stdin, stdout

class Solve:
  def __init__(self):
    R = stdin.readline
    W = stdout.write
    n = int(input())
    a = [int(x) for x in R().split()]
    a.sort()
    s = sum(a)
    W(['NO', 'YES'][s%2 == 0 and s-a[n-1] >= a[n-1]])

def main():
  s = Solve()

main()
