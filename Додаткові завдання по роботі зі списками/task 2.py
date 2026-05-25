line = "2 -1 9 6"
parts = line.split()

total = 0
for part in parts:
    total = total + int(part)

print(total)