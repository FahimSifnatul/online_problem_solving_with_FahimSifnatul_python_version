from sys import stdin,stdout

class Grade:
    a,b = 0,0
    def __lt__(self,other):
        return self.b < other.b
n,r,avg = map(int,stdin.readline().split())
grade,add,cnt = [ Grade() for i in range(n) ], 0, 0
for i in range(n):
    grade[i].a, grade[i].b = map(int,stdin.readline().split())
    add += grade[i].a    
grade.sort()
add = n*avg - add if n*avg - add > 0 else 0
for i in range(n):
    if add - r + grade[i].a >= 0:
        add -= (r - grade[i].a)
        cnt += grade[i].b*(r-grade[i].a)
    else:
        cnt += grade[i].b*add
        break
stdout.write('%d' % cnt)    
        

 
