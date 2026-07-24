a=[1,4,7,89,54,34,76,2,642,79,-8,-2,-3]
smallest=a[0]
for i in range(len(a)):
    if a[i]<smallest:
        smallest=a[i]
print("Smallest element in list is",smallest)