a=int(input())
arr=list(map(int,input().strip().split()))
c=0
c1=0
for i in range(a):
    if(arr[i]%2==0):
        c=c+1
    elif(arr[i]%2==1):
        c1=c1+1
print(c,c1)