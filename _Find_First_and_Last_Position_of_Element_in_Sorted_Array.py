n=int(input())
arr=list(map(int,input().split()))
k=int(input())
f=0
for i in range(n):
    if(arr[i]==k):
        f=1
        print(i,end=" ")
        break
for i in range(n-1,-1,-1):
    if(arr[i]==k):
        f=1
        print(i,end="")
        break
if(f==0):
    print("-1 -1")