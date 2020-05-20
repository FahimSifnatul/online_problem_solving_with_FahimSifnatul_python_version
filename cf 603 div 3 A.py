for i in range(int(input())):
  a,b,c = sorted(map(int,input().split()))
  b = b-1 if b-a > 1 else (b+1 if c-b > 1 else b)
  a = a+1 if a < b else a
  c = c-1 if b < c else c
  print((c-a)<<1)
