from sys import stdin, stdout

class Solve:
  def __init__(self):
    R = stdin.readline
    W = stdout.write
    n, k = map(int, R().split())
    a = [int(x) for x in R().split()]
    a.sort()
    

def main():
  s = Solve()

main()
