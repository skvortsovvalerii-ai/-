first_line = input().split()
n = int(first_line[0])
m = int(first_line[1])

ira_set = set()
for i in range(n):
    color = int(input())
    ira_set.add(color)

igor_set = set()
for i in range(m):
    color = int(input())
    igor_set.add(color)

both = ira_set & igor_set
print(len(both))
for color in sorted(both):
    print(color)

only_ira = ira_set - igor_set
print(len(only_ira))
for color in sorted(only_ira):
    print(color)

only_igor = igor_set - ira_set
print(len(only_igor))
for color in sorted(only_igor):
    print(color)