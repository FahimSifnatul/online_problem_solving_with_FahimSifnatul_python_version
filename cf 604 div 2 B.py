for i in range(int(input())):
  n,s = int(input()), []
  a = [int(x) for x in input().split()]
  a = [(a[i],i+1) for i in range(n)]
  a.sort(key = lambda x : x[0])
  mi = ma = a[0][1]
  for j in range(n):
    mi = min(mi,a[j][1])
    ma = max(ma,a[j][1])
    s.append('1' if ma-mi==j else '0')
  print(''.join(s))
               
