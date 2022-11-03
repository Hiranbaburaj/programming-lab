#exchange 1st and last characters of a string

l1=[]
b=len(a)
a=input("Enter a word: ")
for i in range(b):
    l1.append(a[i])
l2=l1.copy()
l1[0],l1[b-1] = l1[b-1],l1[0]
print(''.join(l1)) 
