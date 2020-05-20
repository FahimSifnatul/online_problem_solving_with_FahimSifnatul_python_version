from sys import stdin, stdout

class Solve:
  def __init__(self):
    r = stdin.readline
    w = stdout.write
    ans = []
    for _ in range(int(input())):
      n = int(r())
      a = [int(x) for x in r().split()]
      pos, neg = 0, 0
      tmp = []
      cnt = 0
      for num in a:
        if pos == 0 and neg == 0:
          tmp.append(num)
          if num > 0:
            pos = 1
          else:
            neg = 1
        else:
          if num > 0 and pos:
            tmp.append(num)
          elif num < 0 and neg:
            tmp.append(num)
          else:
            pos ^= 1
            neg ^= 1
            cnt += max(tmp)
            tmp = [num]
      cnt += max(tmp)
      #print(cnt)
      ans.append(str(cnt))
          
    w('\n'.join(ans))

def main():
  s = Solve()

main()
