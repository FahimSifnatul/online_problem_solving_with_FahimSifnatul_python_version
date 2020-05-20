for i in range(int(input())):
  a, b = map(int, input().split())
  d = abs(a-b)
  print(d//5 + (d%5)//2 + (d%5)%2)
