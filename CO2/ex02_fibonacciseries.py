#Generate Fibonacci series of N terms  
def fib(n):
    a=0
    b=1
    while(n>=1):
        print(a)
        n-=1
        a,b = b,a+b
n=int(input("Enter the number to find the fibonacci series of: "))        
fib(n)