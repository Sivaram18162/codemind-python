s=input()
h=[]
for i in s:
    if i not in h:
        h.append(i)
c=[]
f=0
for i in h:
    if i in "aeiouAEIOU":
        f=1
        c.append(i)
if(f==1):
    print(*c)
else:
    print(-1)