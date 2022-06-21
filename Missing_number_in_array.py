t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    b=set(range(1,n+1))
    print(*b.difference(arr))