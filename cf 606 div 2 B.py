from sys import stdin, stdout
ANS = []
for i in range(int(input())):
  n = int(input())
  a = [int(x) for x in stdin.readline().split()]
  d,ans = dict(), 0
  for j in range(len(a)):
    while a[j]%2 == 0 and (a[j] not in d):
      d[a[j]] = True
      a[j] //= 2
      ans += 1
  ANS.append(str(ans))
stdout.write('\n'.join(ANS))  
