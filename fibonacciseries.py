n=int(input("Enter the number to find the fibonacci series of: "))
a=0
b=1
if n == 1:
    print(0)

elif n == 2:
    print(0)
    print(1)    


else:
    print(0)
    print(1)
    for i in range(n-2):
        c=a+b
        a=b
        b=c
        print(c)
