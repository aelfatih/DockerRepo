#1. Create a new folder in vscode.
#2. Create a new file

#3. Paste this program in file - "employee.py"

employees = []

def add_employee(name, age, department, position):
    employees.append({"name": name, "age": age, "department": department, "position":position})

def view_employees():
    for employee in employees:
        print(f"Name: {employee['name']}, Age: {employee['age']}, Department: {employee['department']}, Position: {employee['position']}")


def search_employee(name):
    for employee in employees:
        if employee["name"].lower() == name.lower():
            print(f"Name: {employee['name']}, Age: {employee['age']}, Department: {employee['department']}, Position: {employee['position']}")
            return
    print("Employee not found!!")

add_employee("Aayam", 29, "IT", "Developer")
add_employee("Ahmed", 39, "IT", "Developer")

print("All Employees: ")
view_employees()

search_employee("Aayam")


# DockerRepo

This is first Git Repository of Docker Repo. This Repository have python projects and database projects.

---------------------------------------------------------------------------------------------------------------------------------------------------------
Git Commands:
-------------
git init
git commit -m "Add Initial Files."

# You are telling Git to associate the specified URL with remote Repository named "origin"
git remote add origin https://github.com/ammishra08/DockerRepo.git

git remote -v
git branch
git branch -M main
git branch
git push origin main
git push -u origin main

# Any update in existing file
git add .
git status
git commit -m "Updated README"
git push
