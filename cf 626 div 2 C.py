from sys import stdin, stdout

class Solve:
  def __init__(self):
    r = stdin.readline
    w = stdout.write
    n = int(input())
    s = r()
    if n%2:
      w('-1')
      return
    t = 0
    OL, CL, OR, CR = [0 for i in range(n)], [0 for i in range(n)], [0 for i in range(n)], [0 for i in range(n)]
    for i in range(n):
      if s[i] == '(':
        OL[i] += 1
      else:
        CL[i] += 1
      if s[n-1-i] == '(':
        OR[i] += 1
      else:
        CR[i] += 1
    for i in range(n):
      
    w('%d\n' % t)

def main():
  s = Solve()

main()
