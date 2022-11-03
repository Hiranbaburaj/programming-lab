#18) Print out all colors from color-list1 not contained in color-list2

a=input("Enter color list 1:")
a=a.split(",")

b=[]
for i in range(len(a)):
    b.append(a[i])
    
c=input("Enter color list 2:")
c=c.split(",")

d=[]
for i in range(len(c)):
    d.append(c[i])  
    
e=[x for x in b if x not in d]  
print("Colors from color-list1 not contained in color-list2 is: ",e)
