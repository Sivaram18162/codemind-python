n=int(input())
temp=n
k=n*n
c=0
while(n):
    if(n%10!=k%10):
        print("Not an Automorphic Number")
        c+=1
        break
    n=n//10
    k=k//10
if(c==0):
    print("Automorphic Number")