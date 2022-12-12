"""Construct following pattern using nested loop
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
* 
"""
def starpattern(n):
    for i in range(n):
        print(" ")
        for j in range(i+1):
            print("*",end=" ")
    for i in range(n-1,0,-1):
        print(" ")
        for j in range(i,0,-1):
            print("*",end=" ")
n=int(input("Enter the max length of star row: "))
starpattern(n)