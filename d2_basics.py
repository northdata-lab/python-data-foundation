# 1. Lists

employees = ["Sarah", "John", "Mike", "Anna"]

print(employees)
print(employees[0])
print(employees[2])

employees.append("Jenny")
print(employees)

print(len(employees))


employees.append("David")
employees.remove("John")

print(employees)

# 2. for loop
employees = ["Sarah", "John", "Mike", "Anna"]

for employee in employees:
    print(f"Employee: {employee}")

# 3. Dictionary
employee = {
    "name": "Sarah",
    "department": "Data",
    "location": "Toronto",
    "salary": 5500,
    "rating": 4
}

print(employee["name"])
print(f"{employee['name']} works in {employee['department']} and is located in {employee['location']}.")
print(employee["salary"])

# 4. while loop

rating = int(input("Enter rating(1-5): "))

while rating < 1 or rating >5:
    print("Invalid string")
    rating = int(input("Please enter rating again(1-5): "))

print("Valid rating:", rating)
