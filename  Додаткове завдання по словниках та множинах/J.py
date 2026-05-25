first_line = input().split()
n = int(first_line[0])
k = int(first_line[1])

strike_days = set()

for i in range(k):
    party_line = input().split()
    a = int(party_line[0])
    b = int(party_line[1])

    current_day = a
    while current_day <= n:
        is_saturday = (current_day % 7 == 6)
        is_sunday = (current_day % 7 == 0)

        if not is_saturday and not is_sunday:
            strike_days.add(current_day)

        current_day += b

print(len(strike_days))