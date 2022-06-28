def push(arr,n):
    c=0
    for i in range(n):
        if(arr[i]!=0):
            arr[c]=arr[i]
            c=c+1
    while(c<n):
        arr[c]=0
        c=c+1
n=int(input())
arr=list(map(int,input().strip().split()))
push(arr,n)
print(*arr)