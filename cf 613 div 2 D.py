from sys import stdin, stdout

class Solve:
  n, a, __ans, bits = 0, [], '', 0
  def solve(self):
    flg = 1
    for bit in range(self.bits, -1, -1):
      one = zero = 0
      for i in range(self.n):
        one = max(one, self.a[i] ^ (1 << bit)) 
        zero = max(zero, self.a[i])
      if one != zero:
        self.__ans += '1' if one < zero else '0'
      else:
        self.__ans += '1' if flg else '0'
        flg ^= 1 
    xor = int(self.__ans, 2)
    self.__ans = 0
    for i in range(self.n):
      self.__ans = max(self.__ans, xor ^ self.a[i])
    stdout.write('%d\n' % self.__ans)
    
      

def main():
  xor = Solve()
  xor.n = int(input())
  xor.a = [int(x) for x in stdin.readline().split()]
  xor.bits = len(bin(max(xor.a))) - 3 
  xor.solve()

main()
