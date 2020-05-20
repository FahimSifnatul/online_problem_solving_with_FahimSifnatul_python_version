for t in range(int(input())):
  s = input()
  cnt = 0
  pos = -1
  for i in range(len(s)):
    if s[i] == '1':
      if pos == -1:
        pos = i
      else:
        cnt += i - pos - 1
        pos = i
  print(cnt)
