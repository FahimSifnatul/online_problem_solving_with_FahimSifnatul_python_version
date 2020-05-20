from sys import stdin, stdout

class Solve:
  def __init__(self):
    R = stdin.readline
    W = stdout.write
    n, d = [int(x) for x in R().split()]
    a = [int(x) for x in R().split()]
    d %= n
    a = a[d:] + a[:d]
    print(*a)      

def main():
  s = Solve()

main()
