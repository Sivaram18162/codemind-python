a,b=map(int,input().split())
if(a>b):
    a,b=b,a
for i in range(1,b+1):
    if(a%i==0 and b%i==0):
        gcd=i
lcm=a*b//gcd
print(lcm)