s = input("Enter a string:")
a = 0
e = 0
i = 0
o = 0
u = 0
for vowels in s.lower():
    if vowels == "a":
        a += 1
    elif vowels == "e":
        e += 1
    elif vowels == "i":
        i += 1
    elif vowels == "o":
        o += 1
    elif vowels == "u":
        u += 1
print("a comes ",a,"times")
print("e comes",e,"times")
print("i comes",i,"times")
print("o comes",o,"times")
print("u comes",u,"times")