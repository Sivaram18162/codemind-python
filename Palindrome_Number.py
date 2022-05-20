n=int(input())
for i in range(n):
    a=int(input())
    temp=a
    s=0
    while(a):
        d=a%10
        s=s*10+d
        a=a//10
    if(s==temp):
        print("True")
    else:
        print("False")