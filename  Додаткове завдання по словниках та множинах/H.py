n = int(input())

possible_numbers = set()
for i in range(1, n + 1):
    possible_numbers.add(i)

while True:
    line = input()
    if line == "HELP":
        break

    question_set = set()
    for x in line.split():
        question_set.add(int(x))

    intersection = possible_numbers & question_set

    if len(intersection) <= len(possible_numbers) / 2:
        print("NO")
        possible_numbers = possible_numbers - question_set
    else:
        print("YES")
        possible_numbers = possible_numbers & question_set

for number in sorted(possible_numbers):
    print(number, end=" ")