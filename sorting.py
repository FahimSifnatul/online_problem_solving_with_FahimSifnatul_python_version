cmp = lambda x : x[1]

a = [ [1,4], [2,3], [3,2], [4,1] ]
a.sort(key = cmp)
print(a)
