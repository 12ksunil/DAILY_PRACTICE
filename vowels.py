s =input("Enter a String:")
for i in s:
    if i.lower() in "aeiou":
        print(i, "is a vowel")
    else:
        print(i, "is not a vowel")