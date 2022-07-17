t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    arr=list(map(int,input().split()))
    brr=list(map(int,input().split()))
    crr=arr+brr
    crr.sort()
    print(*crr)