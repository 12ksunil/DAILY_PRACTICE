a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c=max(a,b)
d=a*b
for i in range(c,d+1):
    if i%a==0 and i%b==0:
        print("LCM =", i)
        break