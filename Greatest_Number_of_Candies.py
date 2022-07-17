n=int(input())
arr=list(map(int,input().strip().split()))
k=int(input())
I=max(arr)
for i in range(n):
    if(arr[i]+k>=I):
        print(True,end=" ")
    else:
        print(False,end=" ")