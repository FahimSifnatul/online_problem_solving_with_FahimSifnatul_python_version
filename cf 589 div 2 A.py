l, r = map(int, input().split())
for distinct_num in range(l, r+1):
  temp = str(distinct_num)
  if len(temp) == len(set(list(temp))):
    print(distinct_num)
    exit(0)
print(-1)
