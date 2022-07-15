n=input()
if len(n)==len(set(n.lower())):
    print("True")
else:
    print("False")