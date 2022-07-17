a=int(input())
arr=list(map(int,input().split()))
c=0
dc=0
for i in range(a):
    c=0
    while(arr[i]):
        d=arr[i]%10
        c=c+1
        arr[i]=arr[i]//10
    if(c%2==0):
        dc=dc+1
print(dc)