# 16) Create a list of colors from comma seprated color names entered by user. Display first and last colors

a=input("Enter the colors:")
a=a.split(",")

b=[]
for i in range(len(a)):
    b.append(a[i])
    
print(b[0],b[len(a)-1]) 
