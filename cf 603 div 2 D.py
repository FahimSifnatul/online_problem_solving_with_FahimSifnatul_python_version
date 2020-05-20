from sys import stdin
a = [-1*i for i in range(27)]
st = set()
for i in range(int(input())):
  s,flg = stdin.readline(), 0
  l = len(s)-1
  for j in range(l):
    o = ord(s[j])-96
    if a[o] > 0:
      st.add(s[j])
      flg = 1
      break
  if not flg:
    o = ord(s[0])-96
    st.add(s[0])
    a[o] = o
  for j in range(l):
    a[ord(s[j])-96] = a[o]

s = set()
for x in st:
  if a[ord(x)-96] > 0:
    s.add(a[ord(x)-96])
print(len(s))
