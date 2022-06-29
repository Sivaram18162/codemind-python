n=int(input())
temp=n
s=0
rem=0
while(s!=1 and s!=4):
    s=0
    while(temp!=0):
        r=temp%10
        s=s+r*r
        temp=temp//10
    temp=s
if(s==1):
    print("True")
else:
    print("False")