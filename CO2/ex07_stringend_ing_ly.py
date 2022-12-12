#Add ‘ing’ at the end of a given string. If it already ends with ‘ing’, then add ‘ly’
def stringend(a):
    if a[-3:]=="ing":
        print(a+"ly")
    else:
        print(a+"ing")
stringend(input("Enter the word: "))  