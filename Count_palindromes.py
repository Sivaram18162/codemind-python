def pal(n):
    s=0
    temp=n
    while(n!=0):
        d=n%10
        s=s*10+d
        n=n//10
    if(s==temp):
        return 1
    else:
        return 0
k=int(input())
a=list(map(int,input().split()))
c=0
for i in range(k):
    if pal(a[i]):
        c=c+1
print(c)