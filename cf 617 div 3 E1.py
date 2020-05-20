from sys import stdin, stdout
 
class Solve:
  def __init__(self):
    R = stdin.readline
    W = stdout.write
    n = int(input())
    s = [x for x in R()]
    s.pop()
    tmps = [] + s
    sor = sorted(s)
    ans = ['0' for i in range(n)]
    for i in range(n):
      if s[i] != sor[i]:
        flg = 0
        for j in range(i+1,n):
          if s[j] == sor[i]:
            for k in range(j, i, -1):
              s[k] = s[k-1]
              if k == j:
                ans[k] = '1'
            s[i] = sor[i]
            break
    tmpans = [] + ans
    for i in range(n):
      if tmps[i] != sor[i]:
        for j in range(i,n):
          if tmps[j] == sor[i]:
            for k in range(j, i, -1):
              if tmpans[k] != tmpans[k-1]:
                tmpans[k], tmpans[k-1] = tmpans[k-1], tmpans[k]
                tmps[k], tmps[k-1] = tmps[k-1], tmps[k]
    if tmps != sor:
      W('NO')
      return
    W('YES\n')
    W(''.join(ans))
 
def main():
  s = Solve()
 
main()











