d1={}
n=int(input("Enter no of items in dictionary 1: "))

for i in range(n):
    key=input("Enter the Key: ")
    value=input("Enter the Value: ")
    d1[key]=value

print(d1)

d2={}
n=int(input("Enter no of items in dictionary 2: "))

for i in range(n):
    key=input("Enter the Key: ")
    value=input("Enter the Value: ")
    d2[key]=value

print(d2) 

d3={**d1,**d2}
for k,v in d3.items():
    if k in d1 and k in d2:
        d3[k] =[v,d1[k]]

print(d3)        
