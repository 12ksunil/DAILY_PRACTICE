s=input("Enter a string:")
count_upper=0
count_lower=0
for i in s:
    if i in s.upper():
        count_upper +=1
    elif i in s.lower():
        count_lower +=1
print("Upper_case is",count_upper)
print("Lower_case is",count_lower)