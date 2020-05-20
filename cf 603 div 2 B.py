for i in range(int(input())):
  n,chng = int(input()), 0
  a = []
  for j in range(n):
    a.append(list(input()))
  for j in range(n):
    flg, tmp, num = 1, 0, a[j][3]
    while flg:
      for k in range(n):
        if j != k and a[j] == a[k]:
          a[j][3] = str(tmp)
          flg = 0
          break
      if a.count(a[j]) == 1 and flg:
        flg = 0
      elif a.count(a[j]) == 1 and not flg:
        chng += 1
      else:
        flg, tmp = 1, tmp+1
        a[j][3] = num
      
  print(chng)
  for j in range(n):
    print(''.join(a[j]))
        
    
