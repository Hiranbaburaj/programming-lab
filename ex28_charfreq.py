def freq(a):
    s=a.lower()
    ln=len(s)
    l1=[]
    d={}
    for i in range(0,ln):
        if s[i]!= ' ':
            l1.append(s[i])
    for w in l1:
        if w in d:
            d[w]+=1
        else:
            d[w]=1
    print(d)

a=input("Enter the string: ")
freq(a)