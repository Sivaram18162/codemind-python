def fib(n):
    a,b=0,1
    if(n<=1):
        return n
    return fib(n-1)+fib(n-2)
n=int(input())
for i in range(n):
    print(fib(i),end=" ")