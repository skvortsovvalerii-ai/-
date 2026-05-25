line1 = input()
line2 = input()

set1 = set(line1.split())
set2 = set(line2.split())

common_elements = set1 & set2

print(len(common_elements))