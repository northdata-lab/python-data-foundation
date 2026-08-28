#Employee performance report

employees = [{
    "name": "Sarah",
    "department": "Data",
    "salary": 5000,
    "rating": 5
},
{
    "name": "John",
    "department": "Finance",
    "salary": 4500,
    "rating": 3
},
{
    "name": "Anna",
    "department": "HR",
    "salary": 4200,
    "rating": 4
}
]

for employee in employees:
    annual_salary = employee["salary"]*12

    if employee["rating"] >=5:
        performance = "High performance"
    elif employee["rating"] >=3:
        performance = "Meets expectations"
    else:
        performance = "Needs improvement"


    print(f"Employee: {employee['name']}")
    print(f"Department: {employee['department']}")
    print(f"Annual Salary: ${annual_salary:,.2f}")
    print(f"Performance: {performance}")
    print("-" *30)