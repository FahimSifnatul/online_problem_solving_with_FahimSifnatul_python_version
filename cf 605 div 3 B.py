from sys import stdin, stdout
for i in range(int(input())):
  s = stdin.readline()
  r = s.count('R')
  u = s.count('U')
  l = s.count('L')
  d = s.count('D')
  
  r = l = min(r,l)
  u = d = min(u,d)

  if r == u == 0:
    stdout.write('0\n')
  elif r == 0 or u == 0:
    stdout.write('2\n')
    stdout.write('%s\n' % ('UD' if r == 0 else 'RL'))
  else:
    stdout.write('%d\n' % ((r+u)<<1))
    s = ['R' for i in range(r)] + ['U' for i in range(u)] + ['L' for i in range(l)] + ['D' for i in range(d)]
    stdout.write(''.join(s))
  stdout.write('\n') 
