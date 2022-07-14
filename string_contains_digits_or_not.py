n=int(input())
for i in range(n):
    s=input()
    c=0
    for j in s:
        if j.isdigit():
            c=c+1
    if(c==0):
        print("No")
    else:
        print("Yes")