#21) Find GCD of 2 numbers 
x=int(input("Enter 1st number: "))
y=int(input("Enter 2nd number: "))
if(x<y):
    smaller=x
else:
    smaller=y

for i in range(1,smaller+1):
    if((x%i==0) and (y%i==0)):
        gcd=i
print("The GCD of",x,"&",y,"is",gcd) 
