a = [1,2,3,4,4,4,5,5,5,3,2]
c = []
for i in range(len(a)):
    if a[i] not in c:
        b = 1
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                b=b+1
        print(a[i],b)
        c.append(a[i])