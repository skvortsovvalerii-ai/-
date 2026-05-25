sales_database = {}

while True:
    line = input()
    if line == "":
        break

    parts = line.split()
    customer = parts[0]
    item = parts[1]
    quantity = int(parts[2])

    if customer not in sales_database:
        sales_database[customer] = {}

    if item not in sales_database[customer]:
        sales_database[customer][item] = quantity
    else:
        sales_database[customer][item] += quantity

all_customers = list(sales_database.keys())
all_customers.sort()

for customer in all_customers:
    print(customer + ":")

    all_items = list(sales_database[customer].keys())
    all_items.sort()

    for item in all_items:
        print(item, sales_database[customer][item])