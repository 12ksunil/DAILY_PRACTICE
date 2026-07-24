s = "Hello"

for ch in s:
    if ch.lower() in "aeiou":
        print(ch, "is a vowel")
    else:
        print(ch, "is not a vowel")