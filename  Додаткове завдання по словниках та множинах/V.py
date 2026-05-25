n = int(input())
state_electors = {}
for i in range(n):
    parts = input().split()
    state_electors[parts[0]] = int(parts[1])

state_votes = {}
all_candidates = set()

while True:
    line = input()
    if line == "":
        break
    state, candidate = line.split()
    all_candidates.add(candidate)

    if state not in state_votes:
        state_votes[state] = {}
    if candidate not in state_votes[state]:
        state_votes[state][candidate] = 1
    else:
        state_votes[state][candidate] += 1

final_summary = {}
for candidate in all_candidates:
    final_summary[candidate] = 0

for state in state_votes:
    candidate_votes = state_votes[state]

    winner = ""
    max_votes = -1

    for candidate in candidate_votes:
        votes_count = candidate_votes[candidate]
        if votes_count > max_votes:
            max_votes = votes_count
            winner = candidate
        elif votes_count == max_votes:
            if candidate < winner:
                winner = candidate

    final_summary[winner] += state_electors[state]

final_sorting_list = []
for candidate in final_summary:
    final_sorting_list.append((-final_summary[candidate], candidate))
final_sorting_list.sort()

for element in final_sorting_list:
    electors_received = -element[0]
    candidate_name = element[1]
    print(candidate_name, electors_received)