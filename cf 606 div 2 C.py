from sys import stdin,stdout
ans,pos = [], 0
for i in range(int(input())):
  s = stdin.readline()
  cnt, j, l = 0, 0, len(s)-2
  while j <= l-2:
    tmp = s[j] + s[j+1] + s[j+2]
    if j <= l-4 and tmp+s[j+3]+s[j+4] == 'twone':
      ans.append(str(j+3))
      ans.append(' ')
      cnt += 1
      j += 5
    elif tmp in ['one','two']:
      ans.append(str(j+2))
      ans.append(' ')
      cnt += 1
      j += 3
    else:
      j += 1
  ans.append('\n')
  ans.insert(pos, str(cnt))
  ans.insert(pos+1, '\n')
  pos = len(ans)
stdout.write(''.join(ans))
