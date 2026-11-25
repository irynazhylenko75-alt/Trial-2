amount_wanted = input("Enter amount in EUR: ").replace(",", ".")
cents = round(float(amount_wanted)*100)

denominations = [50000, 20000, 10000, 5000, 2000, 1000, 500,
                 200, 100, 50, 20, 10, 5, 2, 1]
total = 0

for d in denominations:
    count = cents // d 
    cents = cents % d
    total = total + count
    if count > 0:
        if d >= 500:
            print(f"{d // 100} EUR banknote: {count}")
        elif d >= 100:
            print(f"{d // 100} EUR coin: {count}")
        else: 
           print(f"{d} cent coin: {count}")
print("Total pieces:", total)
          
