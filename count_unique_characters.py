def uniq(s):
    c=0
    for i in s:
        if(s.count(i)==1):
            c=c+1
    return c
s=input()
s=s.lower().replace(" ","")
print(uniq(s))