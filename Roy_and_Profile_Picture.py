I=int(input())
n=int(input())
for i in range(n):
    w,h=map(int,input().split())
    if(w<I or h<I):
        print("UPLOAD ANOTHER")
    elif(w==h):
        print("ACCEPTED")
    elif(w==h and h==I):
        print("ACCEPTED")
    elif(w>I or h>I):
        print("CROP IT")