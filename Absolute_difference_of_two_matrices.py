r=int(input())
m1=[list(map(int,input().strip().split())) for i in range(r)]
m2=[list(map(int,input().strip().split())) for i in range(r)]
c=[]
for i in range(r):
    a=[]
    for j in range(r):
        d=abs(m1[i][j]-m2[i][j])
        a.append(d)
    c.append(a)
for i in c:
    print(*i)