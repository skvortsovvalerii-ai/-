a = input()

digits = []
for p in a:
    if p != " ":
        digits.append(int(p))

digits_copy = digits.copy()
digits_copy.sort()
digits_copy.reverse()

number_str = ""
for d in digits_copy:
    number_str = number_str + str(d)

print(int(number_str))