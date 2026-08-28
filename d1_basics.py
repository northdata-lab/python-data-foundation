name = "Sarah Connor"
age = 38
salary = 5000.50
learning_python = True

# Variables + data types
print(name)
print(age)
print(salary)
print(learning_python)

print(type(name))
print(type(age))
print(type(salary))
print(type(learning_python))


monthly_salary = 5000
annual_salary = monthly_salary *12
bonus = annual_salary *0.1
total_compensation = annual_salary + bonus

# Basic calculation practice
print(annual_salary)
print(bonus)
print(total_compensation)

# f-string practice
print(f"{name}'s annual salary is ${annual_salary}")

print(f"{name}'s total compansition is ${total_compensation}")

#input() practice
name = input("Enter employee name: ")
monthly_salary = float(input("Enter monthly salary: "))

annual_salary = monthly_salary *12

print(f"{name}'s annual salary is ${annual_salary}")

# if/elif/else

rating = int(input("Enter performance rating (1-5): "))

if rating >= 5:
    print("High Performer")
elif rating >=3:
    print("Meets Expectations")
else:
    print("Needs Improvement")

    