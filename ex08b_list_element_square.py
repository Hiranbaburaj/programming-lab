#square of list elements using list comprehension
a=[1, 2, 3, -1, -2, 4, 5, -9]
b=[x*x for x in a if x>0]
print(b)
