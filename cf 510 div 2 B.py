from sys import stdin,stdout

def ok(n,s):
    st = ''.join(sorted(s)) 
    d[st] = min(d[st], int(n))

d = { 'A': 10000000, 'B' : 10000000, 'C' : 10000000,
      'AB' : 10000000, 'BC' : 10000000, 'AC' : 10000000,
      'ABC' : 10000000 }
a = [ (lambda n,s : ok(n,s))(*stdin.readline().split()) for i in range(int(stdin.readline())) ]
a[0] = min(d['A']+d['B']+d['C'],
           d['A'] + d['BC'], d['B'] + d['AC'], d['C'] + d['AB'],
           d['AB']+d['BC'],d['AC']+d['AB'],d['AC']+d['BC'],
           d['ABC'])
stdout.write( '%d' % (-1 if a[0] >= 10000000 else a[0]) )
