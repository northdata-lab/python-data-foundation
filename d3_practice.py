# Changing Day 2 Employee Performance Report into function
# Function declaration, return, loop, dictionary access, function call, variable assignment

employees = [{
    "name": "Sarah",
    "department":"Data",
    "salary": 5000,
    "bonus": 10,
    "rating": 5
},
{
    "name": "John",
    "department": "Finance",
    "salary": 4500,
    "bonus": 5,
    "rating": 3
},
{
    "name": "Anna",
    "department": "HR",
    "salary": 4200,
    "bonus": 20,
    "rating": 4
}
]

def calculate_annual_salary(salary):
    annual_salary_calculator = salary * 12

    return annual_salary_calculator

def calculate_bonus(salary, bonus):
    bonus_calculator = salary * 12 * bonus / 100

    return bonus_calculator

def get_performance(rating):
      if rating >=5:
        return "High Performance"
      elif rating >=3:
        return "Meets Expectations"
      else:
         return "Low Expectations"

for employee in employees:
    annual_salary = calculate_annual_salary(employee['salary'])
    bonus = calculate_bonus(employee['salary'], employee['bonus'])
    performance = get_performance(employee['rating'])


    print(f"Employee: {employee['name']}")
    print(f"Department: {employee['department']}")
    print(f"Annual Salary: ${annual_salary:,.2f}")
    print(f"Bonus: ${bonus:,.2f}")
    print(f"Performance: {performance}")
    print("-"*30)