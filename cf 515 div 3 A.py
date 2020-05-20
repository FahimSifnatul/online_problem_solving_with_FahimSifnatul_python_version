from sys import stdin,stdout

def main():
    n,r = map(int,stdin.readline().split())
    a = list( map(int,stdin.readline().split()) )
    heaters = 0
    heaters_ok = [ 0 for i in range(1005)]
    for i in range(n): 
        if a[0] == 1:
            heaters += 1
            l = min(n-1,i + r - 1)
            for j in range(i+1,l+1):
                if a[j] == 0:
                    heaters_ok[j] += 1
            l = max(0,i - r + 1)
            for j in range(l,i):
                if a[j] == 0:
                    heaters_ok[j] += 1
     for i in range(n):
         if a[i] == 0 and heaters_ok[i] == 0:
             stdout.write('%d' % -1)
             return 0
         else:
             
            
   
main()
   
