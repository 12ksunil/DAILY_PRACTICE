a=[1,2,3,4,5,6,7,8,9,8,7,6,5,4,2]
b=[]
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
print(b)
