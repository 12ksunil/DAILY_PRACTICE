n=input("Enter a number:")
sum=0
a=len(n)
for i in n:
    sum=sum + int(i)**a
if sum == n:
    print("Number is armstrong")
else:
    print("Number is not armstrong")