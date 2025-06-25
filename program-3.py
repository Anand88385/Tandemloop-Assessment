a = int(input("Enter a: "))

if a % 2 == 0:
    count = a - 1
else:
    count = a
i = 1
printed = 0

while printed < count:
    print(i, end=", ")
    i = i + 2
    printed = printed + 1
