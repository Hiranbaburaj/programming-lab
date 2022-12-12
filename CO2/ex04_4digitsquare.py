#Generate a list of four digit numbers in a given range with all their digits even and the number is a perfect square. 
def fourdigitsquare(n):
    e=[]
    for i in range(1000,n):
        c=[x for x in str(i)]
        k=[]
        for j in range(len(c)):
            if int(c[j])%2==0:
                k.append(c[j])
            if len(k) == len(c):
                if i**0.5 == int(i**0.5):
                    e.append(i)
    print(e)
n=int(input("Enter the maximum range: "))
if n>=1000:
    fourdigitsquare(n)
else:
    print("Enter a number above 1000")
