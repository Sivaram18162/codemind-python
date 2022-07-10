s=input()
I=input()
for i in I.split():
    for j in s.split():
        if(i.lower()==j.lower()):
            print(j.lower(),end=" ")