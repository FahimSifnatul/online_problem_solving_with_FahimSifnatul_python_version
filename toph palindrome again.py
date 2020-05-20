n={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,'twenty':20,'thirty':30,'forty':40,'fifty':50,'sixty':60,'seventy':70,'eighty':80,'ninety':90,'hundred':100,'thousand':1000}
for t in range(int(input())):
 l,a=list(map(lambda x:n[x],input().split())),0;L=len(l)
 for i in range(0,L,2):
  a+=l[i]if i==L-1 else(l[i]*l[i+1]if l[i+1]in[100,1000]else l[i]+l[i+1])
 a=str(bin(a))+'b0';print('YES'if a==a[::-1]else'NO')
