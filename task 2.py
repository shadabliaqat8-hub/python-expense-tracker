total = 0

while True:
    expense = input("Enter expense (or type 'done' to finish): ")

    if expense == "done":
        break

    expense = float(expense)
    total = total + expense

print("Total Spent:", total)