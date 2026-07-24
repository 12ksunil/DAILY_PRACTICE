a=[1,2,3,4,5,6,7,8,9,8,7,6,5,4,2]
b=[]
for i in range(len(a)):
    for j in range(i+1):
        if a[i]==a[j]:
            print(a[i],end="")
        b.append(a[i])