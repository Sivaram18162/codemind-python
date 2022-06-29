n=int(input())
k=n*n
sum=0
while(k):
    d=k%10
    sum=sum+d
    k=k//10
if(n==sum):
    print("Neon Number")
else:
    print("Not Neon Number")