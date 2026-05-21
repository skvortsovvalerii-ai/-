cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']

result = ""
for i in range(len(cities) - 1):
    result = result + cities[i]
    if i < len(cities) - 2:
        result = result + ", "

result = result + " and " + cities[-1]

print(result)