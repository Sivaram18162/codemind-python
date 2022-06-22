import math
a=int(input())
for i in range(a):
    b=int(input())
    s=int(math.sqrt(b))
    if(s*s==b):
        print("True")
    else:
        print("False")