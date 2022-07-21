n=int(input())
arr=list(map(int,input().split()))
k=[]
for i in range(len(arr)):
    k.append(sum([int(i) for i in str(arr[i])]))
print(sum(k))