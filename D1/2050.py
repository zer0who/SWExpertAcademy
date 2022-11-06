alphabets = input()
print(alphabets)
for i in range(len(alphabets)):
    print(ascii(alphabets[i], end = " "))