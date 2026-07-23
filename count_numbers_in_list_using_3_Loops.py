a = [1,2,3,3,4,4,5,5,5,3,2,1]
for i in range(len(a)):          
    b=1
    for j in range(i+1,len(a)):      
        if a[i]==a[j]:
            b=b+1
    x=True
    for k in range(i):           
        if a[i]==a[k]:
            x=False
            break
    if x:
        print(a[i],b)