employees = [
    {"name":"Tony", "Salary":50000.00, "rating":5},
    {"name":"Steves", "Salary":45000.00, "rating":3},
    {"name":"Natasha", "Salary":40000.00, "rating":1},
    {"name":"Bruce", "Salary":48000.00, "rating":2}
]
print(employees)

salary_hike = lambda emp : {
    "name" : emp["name"], 
    "Salary": round(emp["Salary"] * 1.10) if emp["rating"] in [4, 5] else
              emp["Salary"] * 1.05 if  emp["rating"] == 3 else
              emp["Salary"] * 0.97,
    "rating": emp["rating"]
}
update_employees = list(map(salary_hike, employees))

for emp in update_employees:
    print(f"{emp['name']}'s new salary: {emp['Salary'] }")