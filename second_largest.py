a=[1,2,3,4,5,6,88,7,8,9,10,99]
b=[]
largest=0
for i in range(len(a)):
    if a[i] > largest:
        largest = a[i]
        b.append(a[i])
print(b)
for i in range(len(b)-2,0,-1):
    print(b[i])
    break

