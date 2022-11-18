def fib(n):
    a=0
    b=1
    for i in range(n):
        print(a)
        c=a+b
        a=b
        b=c
        
n=int(input("Enter the number to find the fibonacci series of: "))
print(fib(n))
