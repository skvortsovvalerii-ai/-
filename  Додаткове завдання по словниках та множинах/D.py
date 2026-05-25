input_data = input()
all_numbers = input_data.split()

seen_numbers = set()

for number in all_numbers:
    if number in seen_numbers:
        print("YES")
    else:
        print("NO")
        seen_numbers.add(number)