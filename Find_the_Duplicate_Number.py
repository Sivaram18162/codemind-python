n=int(input())
arr=list(map(int,input().strip().split()))
for i in range(n):
    for j in range(i+1,n):
        if(arr[i]==arr[j]):
            print(arr[i])