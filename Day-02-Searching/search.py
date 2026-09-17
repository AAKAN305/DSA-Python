numbers = [5, 12, 8, 20, 15]

target = 20
found = False

for num in numbers:
    if num == target:
        found = True

if found:
    print("Found")
else:
    print("Not Found")
