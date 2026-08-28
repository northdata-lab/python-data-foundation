
# 1. Function
def greet():
    print("Hello Python!")

greet()

# 2. Parameter
# Declare 2 parameters in 1 function. name, department.
def greet_employee(name, department):
    print(f"Hello {name}! You work in {department}.")

greet_employee("Sarah", "Data")
#greet_employee("John")

#3. return
# return function send back the result of the function

def calculate_annual_salary(monthly_salary):
    annual_salary = monthly_salary*12
    return annual_salary

salary = calculate_annual_salary(5000)

print(salary)

def calculate_bonus(annual_salary, bonus_percentage):
    bonus_amount = annual_salary*(bonus_percentage/100)
    return bonus_amount

bonus = calculate_bonus(60000, 5)

print(bonus)

# 4. Performance function

def get_performance(rating):
    if rating >=5:
        return "High Performer"
    elif rating >=3:
        return "Meets Expectations"
    else:
        return "Needs Improvement"

performance = get_performance(4)
print(performance)
