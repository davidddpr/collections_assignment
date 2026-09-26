kwh = int(input("Enter the KW hours used: "))
if kwh <= 1000:
    amount = kwh * 7.633
else:
    amount = (1000 * 7.633) + ((kwh - 1000) * 9.259)
amount = amount / 100
print(f"Amount owed is ${amount:.5f}")
