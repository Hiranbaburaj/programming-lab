#14) Find biggest of 3 numbers entered 

n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
n3=int(input("Enter the third number: "))
if(n1>n2):
    if(n1>n3):
        print(n1,"is the greatest number")
    else:
        print(n3,"is the greatest number")
else:
    if(n2>n3):
        print(n2,"is the greatest number")
    else:
        print(n3,"is the greatest number")
