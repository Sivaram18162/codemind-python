n=int(input())
arr=list(map(int,input().strip().split()))
k=int(input())
f=0
for i in range(n):
    if(arr[i]==k):
        f=1
        print(i)
if(f==0):
    print("-1")