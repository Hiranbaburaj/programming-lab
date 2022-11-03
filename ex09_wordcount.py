d={}
a=input("Enter the sentence you want to print: ")
l=a.lower()
words=l.split()
for w in words:
    if w in d:
        d[w]+=1
    else:
        d[w]=1

print(d)        
