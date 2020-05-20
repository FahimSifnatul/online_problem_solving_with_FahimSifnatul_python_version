from math import gcd

t = int(input())
while t:
        t -= 1
        n,d,b = map(int,input().split())
        d //= gcd(n,d)
        while True:
            g = gcd(d,b)
            if g == 1:
                if d > 1:
                    stdout.write('Infinite\n')
                else:
                    stdout.write('Finite\n')
                break        
            while not d % g:
                d //= g










