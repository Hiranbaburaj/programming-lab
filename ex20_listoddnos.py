#20) From a list of integers, Create a list removing even numbers 
a=input("Enter the list of integers : ")
a=a.split(" ")
b=[]
for i in a:
    if (int(i)%2!=0):
        b.append(int(i))
print(b)
