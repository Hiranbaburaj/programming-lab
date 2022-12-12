#Accept a list of words and return length of longest word. 
def maxln(a):
    ln=a.split(' ')
    l1=[]
    for i in ln:
        l1.append(len(i))
    print("The length of the longest word is: ",max(l1))
a=input("Enter the list of words(seperate by space): ")
maxln(a) 