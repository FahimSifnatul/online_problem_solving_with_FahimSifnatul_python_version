s, k, l, cane, snow, ans = list(input()), int(input()), 0, 0, 0, list()
for i in range(len(s)):
    l += 1 if s[i+1] != '?' or s[i+1] != '*' else 0
    cane += 1 if s[i+1] == '?' else 0
    snow += 1 if s[i+1] == '*' else 0
if k < l:
    print('Impossible')
else:
    for i in range(len(s)):
        


