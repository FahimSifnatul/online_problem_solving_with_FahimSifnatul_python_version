for i in range(int(input())):
  s = input()
  res, l, j = [], len(s), 0
  while j < l:
    if j == l - 1:
      res += s[j]
      j += 1
    elif s[j] == s[j+1]:
      j += 2
    else:
      res += s[j]
      j += 1
  res.sort()
  print(''.join(res))
