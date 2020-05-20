from sys import stdin,stdout

def main():
    q = int(stdin.readline())
    query = {}
    l = r = 200005
    while q:
        q -= 1
        char,book = stdin.readline().split() 
        if char == 'L':
            if l == r:
                r += 1
            query.setdefault(book,l)
            l -= 1
        elif char == 'R':
            if l == r:
                l -= 1
            query.setdefault(book,r)
            r += 1
        else:
            stdout.write('%d\n' % min( query[book] - (l + 1), (r - 1) - query[book]) )

main()         


































