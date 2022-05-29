a,b=map(int,input().split())
I=max(a,b)
c=abs(a-b)
if(c==1 or c==-1):
    print('Yes')
elif(I==10 and c==9 or c==-9):
    print('Yes')
else:
    print('No')