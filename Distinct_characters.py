s=input()
s=s.lower().replace(" ","")
f=[]
for i in s:
    if s.count(i)==1:
        f.append(i)
print("".join(sorted(f)))