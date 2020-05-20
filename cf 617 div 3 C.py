from sys import stdin, stdout

class Solve:
  def __init__(self):
    R = stdin.readline
    W = stdout.write
    ans = []
    for t in range(int(input())):
      n = int(input())
      s = R()
      check = {'0_0' : 0}
      d = {'L' : [-1, 0], 'R' : [1, 0], 'U' : [0, 1], 'D' : [0, -1]}
      x = y = l = r = 0
      dis = 1000000000
      for i in range(n):
        x += d[s[i]][0]
        y += d[s[i]][1]
        tmps = str(x) + '_' + str(y)
        if tmps not in check:
          check[tmps] = i+1
        else:
          if i+1-check[tmps] < dis:
            l, r = check[tmps]+1, i+1
            dis = i+1 - check[tmps]
          check[tmps] = i+1
      if l and r:
        ans.append(str(l)+' '+str(r)+'\n')
      else:
        ans.append('-1\n')
    W(''.join(ans))

def main():
  s = Solve()

main()
