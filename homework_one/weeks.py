week = 7
monday = int(input("Consumption Monday: $"))
tuesday = int(input("Consumption Tuesday: $"))
wednesday = int(input("Consumption Wednesday: $"))
thursday = int(input("Consumption Thursday: $"))
friday = int(input("Consumption Friday: $"))
saturday = int(input("Consumption Saturday: $"))
sunday = int(input("Consumption Sunday: $"))


total_expense = monday + tuesday + wednesday + thursday + friday + saturday + sunday
average_expense = total_expense / week
print(round(average_expense, 1))