s=input()
bc=0
ac=0
lc=0
oc=0
nc=0
for i in s:
    if i=="b":
        bc=bc+1
    elif i=="a":
        ac=ac+1
    elif i=="l":
        lc=lc+1
    elif i=="o":
        oc=oc+1
    elif i=="n":
        nc=nc+1
print(min(bc,ac,lc//2,oc//2,nc))        