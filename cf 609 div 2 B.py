from sys import stdin, stdout

def main():
  n, m = map(int, input().split())
  a = [int(x) for x in stdin.readline().split()]
  b = [int(x) for x in stdin.readline().split()]
  a.sort()
  b.sort()
  s = set()
  for i in range(n):
    for j in range(n):
      if a[j] < b[i]:
        s.add(b[i]-a[j])
      elif a[j] > b[i]:
        s.add(m+b[i]-a[j])
  ans = [0] + list(s)
  ans.sort()
  for i in range(len(ans)):
    tmp = []
    for j in range(n):
      tmp.append((a[j]+ans[i])%m)
    tmp.sort()
    if tmp == b:
      print(tmp[i])
      return 0
main()
