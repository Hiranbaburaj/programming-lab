def sumlist(a):   
    a=a.split(" ")
    b=[]
    for i in a:
        b.append(int(i))
    print(sum(b))    
a=input("Enter the elements of list : ")
sumlist(a)
