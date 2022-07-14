s=input()
c=[]
for i in s:
    c.append(int(i))
d=[]
for i in range(len(c)):
    if(c[i]%2==1):
        d.append(c[i]**2)
for i in d:
    print(i,end="")