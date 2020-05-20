f=[1,1,2,6,24,120,720,5040,40320,362880,3628800]
for t in range(int(input())):
  n,r=input().split();z,n,r=n.count('0'),len(n),int(r);print((f[n]-f[n-1]*z)//f[n-r])
