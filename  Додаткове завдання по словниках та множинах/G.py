n = int(input())

possible_numbers = set()
for i in range(1, n + 1):
    possible_numbers.add(i)

while True:
    question = input()
    if question == "HELP":
        break

    beatrice_set = set()
    for x in question.split():
        beatrice_set.add(int(x))

    answer = input()

    if answer == "YES":
        possible_numbers = possible_numbers & beatrice_set
    else:
        possible_numbers = possible_numbers - beatrice_set

result = sorted(possible_numbers)
for number in result:
    print(number, end=" ")