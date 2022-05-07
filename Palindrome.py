n=int(input())
s=0
temp=n
while n>0:
    d=n%10
    s=s*10+d
    n=n//10
if(s==temp):
    print("True")
else:
    print("False")