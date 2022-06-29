n=int(input())
s=0
mul=1
while(n>0):
    d=n%10
    s=s+d
    mul=mul*d
    n=n//10
if(s==mul):
    print("Spy Number")
else:
    print("Not Spy Number")