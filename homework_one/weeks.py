# weeks = ['Monday',  'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', '']
# monday = int(input("Consumption Monday: $"))
# tuesday = int(input("Consumption Tuesday: $"))
# wednesday = int(input("Consumption Wednesday: $"))
# thursday = int(input("Consumption Thursday: $"))
# friday = int(input("Consumption Friday: $"))
# saturday = int(input("Consumption Saturday: $"))
# sunday = int(input("Consumption Sunday: $"))
#
#
# total_expense = monday + tuesday + wednesday + thursday + friday + saturday + sunday
# average_expense = total_expense / week
# average_expense_rounded = (round(average_expense, 1))
#
# if 1 <= average_expense_rounded <= 200:
#     print(f"Мало потратили: {average_expense_rounded}")
# elif 201 <= average_expense_rounded <= 1000:
#     print(f"Средне потратили: {average_expense_rounded}")
# elif 1001 <= average_expense_rounded:
#     print(f"Много потратили: {average_expense_rounded}")
# else:
#     print(f"Ничего не потратили: {average_expense_rounded}")

weeks = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
chain = 5

while chain >= 1:
    total_expense = []
    for week in weeks:
        get_expense = int(input(f"Сколько вы потратили за {week}: $"))
        total_expense.append(get_expense)

    average_expense = round(sum(total_expense) / len(weeks), 1)
    print(f"В среднем вы тратите за неделю ${average_expense}\n")
    chain -= 1

