from sys import stdin, stdout

class Solve:
  def string(self):
    tmp = ''
    s = stdin.readline().lower()
    for i in range(len(s)-1):
      if s[i] not in [';', '-', '_']:
        tmp += s[i]
    return tmp
    
  def __init__(self):
    R = stdin.readline
    W = stdout.write
    check = {}
    ans = []
    a = self.string()
    b = self.string()
    c = self.string()
    check[a+b+c] = check[a+c+b] = check[b+a+c] = check[b+c+a] = check[c+a+b] = check[c+b+a] = True
    n = int(input())
    for i in range(n):
      s = R().lower()
      tmp = ''
      flg = 0
      for j in range(len(s)-1):
        if s[j] not in [';', '-', '_']:
          tmp += s[j]
        if tmp in check:
          flg += 1
          tmp = ''
      ans.append('ACC' if (tmp == '' and flg == 1) else 'WA')
    W('\n'.join(ans))
        
def main():
  s = Solve()
main()
