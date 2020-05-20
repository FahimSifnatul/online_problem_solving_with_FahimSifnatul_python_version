from sys import stdin, stdout

def main():
  r = stdin.readline
  w = stdout.write
  n = int(input())
  a = [0] + [int(x) for x in r().split()]
  given, taken = [], []
  
  tmp = [0 for i in range(n+1)]
  for i in range(1, n+1):
    if a[i]:
      tmp[a[i]] = i

  for i in range(1, n+1):
    if not tmp[i] and not a[i]:
      taken.append(i)
      given.append(i)
      
  for i in range(1, n+1):
    if not tmp[i] and a[i]:
      taken.append(i)
    if not a[i] and tmp[i]:
      given.append(i)
      
  zero = len(given)
  for i in range(zero-1):
    a[given[i]] = taken[i+1]
  a[given[zero-1]] = taken[0]
    
  for i in range(1, n+1):
    w('%d ' % a[i])

main()







