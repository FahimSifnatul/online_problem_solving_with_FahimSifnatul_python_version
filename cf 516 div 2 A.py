from sys import stdin,stdout

def main():
    a,b,c = map(int,stdin.readline().split())
    cnt = 0
    while a+b <= c or b+c <= a or c+a <= b:
        cnt += 1 
        if a+b <= c:
            if a <= b:
                a += 1
            else:
                b += 1
        elif b+c <= a:
            if b<= c:
                b += 1
            else: 
                c += 1
        else:
            if c <= a:
                c += 1
            else:
                a += 1
    stdout.write('%d' % cnt)
main()    
