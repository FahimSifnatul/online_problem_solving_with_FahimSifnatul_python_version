from sys import stdin, stdout

s = stdin.readline()
n = len(s)
ans = []
ch = s[0]
for i in range(n-1):
    ans.append('Ann' if ch < s[i] else 'Mike')
    ch = min(ch, s[i])

stdout.write('\n'.join(ans))
