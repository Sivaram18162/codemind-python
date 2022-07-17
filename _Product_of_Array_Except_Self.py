a=int(input())
arr=list(map(int,input().split()))
for i in range(a):
    f=1
    for j in range(a):
        if(i!=j):
            f=f*arr[j]
    print(f,end=" ")