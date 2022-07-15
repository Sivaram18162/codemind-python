n=input()
c=0
for i in n.split():
    if(i.lower()==i[::-1].lower()):
        c=c+1
print(c)