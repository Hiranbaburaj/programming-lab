#15) Accept a file name from user and print extension of that

a=input("Enter the filename:")
b=a.split(".")
c=len(b)-1
print("The file type is: .",b[c])
