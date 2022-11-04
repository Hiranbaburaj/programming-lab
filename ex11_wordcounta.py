a=input("Enter the list of words: ")
l1=a.split(" ")
d={}

for x in l1:

    d[x] = x.count("a")

print(d)
