a=int(input())
b=int(input())
for i in range(a,b):
    k=i
    s=0
    while(i):
        d=i%10
        s=s*10+d
        i=i//10
    if(s==k):
        print(s,end=' ')