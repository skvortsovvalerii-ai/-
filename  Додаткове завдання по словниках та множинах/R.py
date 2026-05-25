bank_accounts = {}

while True:
    line = input()
    if line == "" or line == "Exit":
        break

    command = line.split()
    cmd_type = command[0]

    if cmd_type == "DEPOSIT":
        name = command[1]
        amount = int(command[2])
        if name not in bank_accounts:
            bank_accounts[name] = 0
        bank_accounts[name] += amount

    elif cmd_type == "WITHDRAW":
        name = command[1]
        amount = int(command[2])
        if name not in bank_accounts:
            bank_accounts[name] = 0
        bank_accounts[name] -= amount

    elif cmd_type == "BALANCE":
        name = command[1]
        if name in bank_accounts:
            print(bank_accounts[name])
        else:
            print("ERROR")

    elif cmd_type == "TRANSFER":
        sender = command[1]
        receiver = command[2]
        amount = int(command[3])
        if sender not in bank_accounts: bank_accounts[sender] = 0
        if receiver not in bank_accounts: bank_accounts[receiver] = 0
        bank_accounts[sender] -= amount
        bank_accounts[receiver] += amount

    elif cmd_type == "INCOME":
        percent = int(command[1])
        for name in bank_accounts:
            if bank_accounts[name] > 0:
                bank_accounts[name] += int(bank_accounts[name] * percent / 100)