n = int(input())
city_to_country = {}

for i in range(n):
    line = input().split()
    country = line[0]
    cities = line[1:]

    for city in cities:
        city_to_country[city] = country

m = int(input())
for i in range(m):
    query = input()
    print(city_to_country[query])