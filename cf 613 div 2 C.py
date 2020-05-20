from math import sqrt, gcd

class LCM:
  lcm = 0 
  def ab(self):
    n = int(sqrt(self.lcm)) + 1
    for a in range(n, 0, -1):
      if not self.lcm % a:
        b = self.lcm // a
        if gcd(a, b) == 1:
          print(a, b)
          return 0

def main():
  solve = LCM()
  solve.lcm = int(input())
  solve.ab()

main()
