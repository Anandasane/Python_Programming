class Employee:
    def __init__(self,id,name,department,salary):
        self.id=id
        self.name=name
        self.department=department
        self.salary = salary
        print(f"The Id of the Employee is {self.id}")
        print(f"The Name of the Employee is {self.name}")
        print(f"The department of the Employee is {self.department}")
        print(f"The salary of the Employee is {self.salary}")



e=Employee(23,'shubham','HR',30000)
e=Employee(45,'Tushar','Data Manager',500000)