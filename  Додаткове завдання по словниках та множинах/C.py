line1 = input()
line2 = input()

set1 = set(line1.split())
set2 = set(line2.split())

common_strings = set1 & set2

common_integers = []
for item in common_strings:
    common_integers.append(int(item))

common_integers.sort()

for number in common_integers:
    print(number, end=" ")