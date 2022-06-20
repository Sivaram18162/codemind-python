a=int(input())
arr=list(map(int,input().strip().split()))
s=0
for i in range(a):
    s=s+arr[i]
print(s)