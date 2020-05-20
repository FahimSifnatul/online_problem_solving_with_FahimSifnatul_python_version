for t in range(int(input())):
 a,b,c=map(int,input().split());print('Case '+str(t+1)+': '+('A'if a>b and a>c else('B'if b>c and b>a else('C'if c>a and c>b else'Confused'))))
