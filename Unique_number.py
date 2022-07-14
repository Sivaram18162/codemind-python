n=int(input())
a=list(str(n))
b=len(a)
c=set(a)
d=len(c)
if(b==d):
    print("Unique Number")
else:
    print("Not Unique Number")