a=[1,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,90]
largest=a[0]
for i in range(len(a)):
    if a[i] > largest:
        largest=a[i]
print("Largest element in list is :",largest)
    