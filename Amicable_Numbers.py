a=int(input())
b=int(input())
s=0
k=0
for i in range(1,a):
    if(a%i==0):
        s=s+i
for i in range(1,b):
    if(b%i==0):
        k=k+i
if(s==b and k==a):
    print("Amicable")
else:
    print("Not Amicable")