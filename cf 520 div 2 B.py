from math import sqrt,ceil,log
class Solve:
  def __init__(self):
    n = int(input())
    prime = {}
    sq = int(sqrt(n)) + 1
    N, cnt = 1, 0 
    for i in range(2,sq):
      if n%i == 0:
        prime[i] = 0
        N *= i
        while n%i == 0:
          n //= i
          prime[i] += 1
    if n > 1:
      prime[n] = 1
      N *= n
    mx, mn = 0, 35
    for data in prime:
      mx = max(mx, prime[data])
      mn = min(mn, prime[data])
    if N == 1:
      cnt = 0
    else:
      cnt = int(ceil(log(mx, 2))) + (0 if mx == mn and mx in [1,2,4,8,16] else 1) 
    print(N, cnt)
    

def main():
  s = Solve()

main()
