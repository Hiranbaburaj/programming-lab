#Generate all factors of a number. 
def factor(a):
    l=[]
    for i in range(1,a):
        if a%i==0:
            l.append(i)
    print("The factors of",a,"are",l)
a=int(input("Enter the number to find all of it's factors: "))
factor(a)