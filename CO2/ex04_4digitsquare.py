#Generate a list of four digit numbers in a given range with all their digits even and the number is a perfect square. 
def perfectsquare(n1,n2):
    a=[x*x for x in range(32,100) if x%2==0]
    #print(a)
    j=len(a)
    e=[]
    for i in range(0,j):
        number=a[i]
        d=str(number)
        c=[x for x in d]
        if int(c[0])%2==0 and int(c[1])%2==0 and int(c[2])%2==0 and int(c[3])%2==0:
            e.append(a[i])
    #print(e)
    finallist=[]

    if n1 > 9999 or n1 < 1000:
        print ("entered digit not 4 digit number")

    elif n2 > 9999 or n2 < 1000:
        print ("entered digit not 4 digit number")

    else:
        if n1<n2:
            for i in range(0,4):
                if e[i]>=n1 and e[i]<=n2:
                    finallist.append(e[i])

        else:
            for i in range(0,4):
                if e[i]>=n2 and e[i]<=n1:
                    finallist.append(e[i])

        print(finallist)

n1= int(input("enter the 1st 4 digit number: "))
n2= int(input("enter the 2nd 4 digit number: "))

perfectsquare(n1,n2)