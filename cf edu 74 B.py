from sys import stdin, stdout
ans = []
for i in range(int(input())):
  n, r = [int(x) for x in stdin.readline().split()]
  a = sorted([int(x) for x in stdin.readline().split()], reverse = True)
  count, steps = 1, 0
  for j in range(1, len(a)):
    if a[j] == a[j-1]:
      continue
    elif a[j] - steps <= 0:
      break
    count, steps = count + 1, steps + r
  ans.append(str(count))
stdout.write('\n'.join(ans))
    
