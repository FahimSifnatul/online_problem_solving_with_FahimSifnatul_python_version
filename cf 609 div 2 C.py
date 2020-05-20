from sys import stdout

def main():
  n,k = map(int, input().split())
  s = list(input())
  while 1:
    flg = 1
    for i in range(len(s)-k):
      if s[i] != s[i+k]:
        flg = 0
        break
    if flg:
      print(len(s))
      print(''.join(s))
      return 0
    s = list(str(int(''.join(s))+1))

main()


























