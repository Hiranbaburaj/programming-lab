#Count the number of characters (character frequency) in a string. 
def freq(a):
    l1=[]
    d={}
    for i in range(0,len(a)):
        if s[i]!= ' ':
            l1.append(a[i])
    for w in l1:
        if w in d:
            d[w]+=1
            
        else:
            d[w]=1
            
    print(d)
    
a=input("Enter the string: ")
freq(a)
