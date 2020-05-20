n,l = map(int, input().split())
s = input()
a = input().split()
ans,com = 0,0
for i in range(n):
  if s[i] not in a:
    ans += ((com*(com+1))>>1)
    com = 0
  else:
    com += 1
ans += ((com*(com+1))>>1)
print(ans)
