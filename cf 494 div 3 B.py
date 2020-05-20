from sys import stdin,stdout
def main():
    a,b,x = map(int,stdin.readline().split())
    s = []
    x -= 1
    l = 2
    s.append('1')
    s.append('0')
    a -= 1
    b -= 1
    while x:
        x -=1
        if s[0] != s[l-1]:
            if a >= b:
                if s[0] == '0':
                    s.append('0')
                else:
                    s.insert(0,'0')
                a -= 1    
            else:
                if s[0] == '1':
                    s.append('1')
                else:
                    s.insert(0,'1')
                b -= 1
        else:
            if s[l-1] == '0':
                s.append('1')
                b -= 1
            else:
                s.append('0')
                a -= 1
        l += 1
    for i in range(l):
        stdout.write('%s' % s[i])
        if s[i] == '0':
            while a:
                stdout.write('%s' % '0')
                a -= 1
        else:
            while b:
                stdout.write('%s' % '1')
                b -= 1
main()         























