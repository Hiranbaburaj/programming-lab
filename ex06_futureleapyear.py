#6) Display future leap years from current year to a final year entered by user

a=int(input("Enter the future year: "))
b=[]
for i in range(2022,a):
    if (i%4==0):
        b.append(i)
print(b)        
    
