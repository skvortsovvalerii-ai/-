candidates_votes = {}

while True:
    line = input()
    if line == "":
        break

    parts = line.split()
    name = parts[0]
    votes = int(parts[1])

    if name not in candidates_votes:
        candidates_votes[name] = votes
    else:
        candidates_votes[name] += votes

names_list = list(candidates_votes.keys())
names_list.sort()

for name in names_list:
    print(name, candidates_votes[name])