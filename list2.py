a=input("Enter the elements of list 1: ")
a=a.split(" ")
print(a)
b=[]
for i in a:
    b.append(int(i))
print(b)    

x=input("Enter the elements of list 2: ")
x=x.split(" ")
print(x)
y=[]
for i in x:
    y.append(int(i))
print(y)

if len(b)==len(y):
    print("The lists are of the same length")

else:
    print("The lists are not the same length")

if sum(b)==sum(y):
    print("The sum of lists are same")

else:
    print("The sum of lists are different")    

same=[c for c in b if c in y]

if len(same)==0:
    print("Commmon element does not exist")

else:
        print("Commmon element exist")
