s=input()
s=s.lower().replace(" ","")
f=[]
for i in s:
    if i not in f:
        f.append(i)
print(len(f))