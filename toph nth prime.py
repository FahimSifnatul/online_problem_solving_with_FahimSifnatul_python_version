p,c=[0,2],[1 for i in range(7368790)]
for i in range(3,2716,2):
 for j in range(2*i+i,7368790,2*i):
  c[j]=0
for i in range(3,7368790,2):
 if c[i]:
  p.append(i)
print(p[int(input())])
