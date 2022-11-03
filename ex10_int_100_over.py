l1 = []
l2=[]
a=int(input("Enter the length of list : "))
for i in range(a):
    l1.append(int(input("Enter the integers: ")))

print(l1)

for j in range(a):
    if l1[j]<100:
        l2.append(l1[j])

    else:
        l2.append("Over")

print(l2)        
        
