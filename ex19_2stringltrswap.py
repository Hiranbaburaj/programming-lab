a=input("Enter string 1: ")
b=input("Enter string 2: ")
l1=[]
l2=[]
for x in range(len(a)):
    l1.append(a[x])
for x in range(len(b)):
    l2.append(b[x])

l1[0],l2[0] = l2[0],l1[0]
s=""
t=""
s=s.join(l1)
t=t.join(l2)
l3=[]
l3.append(s)
l3.append(t)


print(' '.join(l3)) 




