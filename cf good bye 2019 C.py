from sys import stdin, stdout

def main():
  r = stdin.readline
  w = stdout.write
  two = 1125899906842624
  twob = '0b100000000000000000000000000000000000000000000000000'
  for t in range(int(input())):
    n = int(input())
    a = [int(x) for x in r().split()]
    add,xor = sum(a),0
    
    
