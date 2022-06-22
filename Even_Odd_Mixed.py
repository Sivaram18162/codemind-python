n=int(input())
o=0
e=0
d=0
while n:
    k=n%10
    if(k%2==0):
        e=e+1
    elif(k%2==1):
        o=o+1
    n=n//10
    d=d+1
if(d==e):
    print("Even")
elif(d==o):
    print("Odd")
else:
    print("Mixed")