# Python code to demonstrate naive method
# to compute factorial
n = int(input("Enter the number"))
fact = 1

for i in range(1,n+1):
	fact = fact * i
	
print ("The factorial of is : ",end="")
print (fact)
