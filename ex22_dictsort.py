n = int(input("Enter the range of dict : "))
d= {}
for i in range(n):
    key = input("Enter key : ")
    value = input("Enter value : ")
    d[key] = value


print("Dictionary Sorted by Keys")
print("Ascending order: ",dict(sorted(d.items())))
print("Descending order: ",dict(sorted(d.items(), reverse=True)))


print("Dictionary Sorted by Values")
print("Ascending order: ",dict(sorted(d.items(), key=lambda item: item[1])))
print("Descending order: ",dict(sorted(d.items(), key=lambda item: item[1], reverse=True)))



