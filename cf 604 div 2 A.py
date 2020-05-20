for i in range(int(input())):
  s = list(input())
  l = len(s)
  for j in range(l):
    if s[j] == '?':
      if j == 0:
        s[j] = 'a' if l == 1 or (s[j+1] in ['?','b','c']) else 'b'
      elif j == l-1:
        s[j] = 'a' if (s[j-1] in ['b','c']) else 'b'
      elif (s[j-1] in ['?','b','c']) and (s[j+1] in ['?','b','c']):
        s[j] = 'a'
      elif (s[j-1] in ['?','a','c']) and (s[j+1] in ['?','a','c']):
        s[j] = 'b'
      else:
        s[j] = 'c'
    if j > 0 and s[j] == s[j-1]:
      s = ['-','1']
      break
  print(''.join(s))
