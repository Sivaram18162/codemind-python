s=input()
I=[]
for i in s.split():
    I.append(len(i))
print(max(I))