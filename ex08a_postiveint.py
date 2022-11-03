#list comprehension
#8a) Generate positive list of numbers from a given list of integers 
a=[1, 2, 3, -1, -2, -3]
b=[x for x in a if x>0]
print(b)
