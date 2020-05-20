from sys import stdin, stdout

class Solve:
  def __init__(self):
    r = stdin.readline
    w = stdout.write
    ans = []
    for _ in range(int(input())):
      n = int(r())
      if n%4 == 0:
        ans.append('YES\n')
        even, total_even = 2, 0
        for i in range(n//2):
          ans.append(str(even) + ' ')
          total_even += even 
          even  += 2
        odd, total_odd = -1, 0
        for i in range(n//2 - 1):
          odd += 2
          total_odd += odd
          ans.append(str(odd) + ' ')
        ans.append(str(total_even - total_odd) + '\n')
      else:
        ans.append('NO\n')
    w(''.join(ans))

def main():
  s = Solve()

main()
