a=input("Enter a word: ")
print(a)
vowels=["a" , "e", "i", "o", "u", "A", "E", "I", "O", "U"]
b=[x for x in a if x in vowels]
print("The vowels are: ",b)    
