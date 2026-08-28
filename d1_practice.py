name = input("Enter employee name: ")
monthly_salary = int(input("Enter monthly salary: "))
bonus_per = float(input("Enter bonus percentage: "))
performance = int(input("Enter performance rating(1-5): "))

# per_rating validation check
if performance < 1 or performance >5:
    print("Invalid rating")

if performance >= 5:
    print("High performance")
elif performance >=3:
    print("Meets expectations")
else:
    print("Low expectaions")

annual_salary = float(monthly_salary * 12)
bonus = float(annual_salary * (bonus_per/100))
total_comp = float(annual_salary + bonus)

print(f"Employee: {name}")
print(f"Annual salary: ${annual_salary:,.2f}")
print(f"Bonus: ${bonus:,.2f}")
print(f"Total compensation: ${total_comp:,.2f}")

