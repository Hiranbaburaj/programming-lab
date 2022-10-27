a=input("Enter the elements of list : ")
a=a.split(" ")
print(a)
b=[]
for i in a:
    if (int(i)>0):
        b.append(int(i))
print(b)    

