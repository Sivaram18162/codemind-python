a=int(input())
arr=list(map(int,input().strip().split()))
for i in range(a):
    if(arr.count(arr[i])>a//2):
        k=arr[i]
print(k)