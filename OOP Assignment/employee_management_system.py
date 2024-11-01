from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display_info(self):
        pass


class Employee(Person):
    def __init__(self, employee_id, name, department, role, salary):
        super().__init__(name)
        self.employee_id = employee_id
        self.department = department
        self.role = role
        self._salary = salary  # Encapsulation: private attribute

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

    def display_info(self):
        print(f"ID: {self.employee_id}, Name: {self.name}, Department: {self.department}, Role: {self.role}, Salary: {self._salary}")

    def update_info(self, name=None, department=None, role=None, salary=None):
        if name:
            self.name = name
        if department:
            self.department = department
        if role:
            self.role = role
        if salary:
            self._salary = salary

class Manager(Employee):
    def display_info(self):
        print(f"Manager ID: {self.employee_id}, Name: {self.name}, Department: {self.department}, Role: {self.role}, Salary: {self._salary}")

class Staff(Employee):
    def display_info(self):
        print(f"Staff ID: {self.employee_id}, Name: {self.name}, Department: {self.department}, Role: {self.role}, Salary: {self._salary}")


class Department:
    def __init__(self, department_id, name):
        self.department_id = department_id
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        employee.department = self.name

    def remove_employee(self, employee_id):
        self.employees = [emp for emp in self.employees if emp.employee_id != employee_id]

    def list_employees(self):
        for emp in self.employees:
            emp.display_info()


class Role:
    def __init__(self, role_id, title, salary_range):
        self.role_id = role_id
        self.title = title
        self.salary_range = salary_range

    def update_salary_range(self, new_range):
        self.salary_range = new_range

# Example usage
if __name__ == "__main__":
    # Create roles
    developer_role = Role(1, "Developer", (50000, 100000))
    manager_role = Role(2, "Manager", (80000, 150000))

    # Create departments
    it_department = Department(1, "IT")
    hr_department = Department(2, "HR")

    # Create employees
    employee1 = Manager(1, "Alice", "IT", "Developer", 70000)
    employee2 = Staff(2, "Bob", "HR", "Manager", 90000)

    # Add employees to departments
    it_department.add_employee(employee1)
    hr_department.add_employee(employee2)

    # List employees in IT department
    print("Employees in IT Department:")
    it_department.list_employees()

    # List employees in HR department
    print("\nEmployees in HR Department:")
    hr_department.list_employees()

   # Documentation
#Employee Management System

#Employee: Represents an employee with attributes like employee_id, name, department, role, and salary.
#Manager: Subclass of Employee with overridden display_info method.
#Staff: Subclass of Employee with overridden display_info method.
#Department: Manages employees within a department.
#Role: Represents a job role with a title and salary range.
#This code meets all the specified requirements, including encapsulation, polymorphism, inheritance, and abstraction. It also includes basic functionality for adding, updating, and listing employees, as well as handling roles and departments. 
