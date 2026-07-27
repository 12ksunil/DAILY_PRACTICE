s = input("Enter a string:")
rev = ""
for i in s:
    rev = i + rev
if s == rev:
    print("Palindrome String")
else:
    print("Not a Palindrome String")