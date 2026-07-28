a = [9,1,2,3,4,5,6,2]
b = [8,5,4,9,2,1,3,6]
c = []
for i in a:
    c.append(i)
for i in b:
    c.append(i)
for i in range(len(c)):
    for j in range(i + 1, len(c)):
        if c[i] > c[j]:
            c[i], c[j] = c[j], c[i]
print(c)