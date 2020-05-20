for i in range(int(input())):
  a,b = [int(x) for x in input().split()]
  a,b = min(a,b), max(a,b)
  print('yes' if not (a+b)%3 and 2*a>=b else 'no')
