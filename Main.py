
from Employee import Employee
from Contract_Employee import ContractEmployee
from Permanent_Employee import PermanentEmployee



Emp1 = PermanentEmployee(209,"Arjun",89000)

Emp2 = ContractEmployee(211,"Abinav",78000)

print("_____________________PermanentEmployee_________________________")

Emp1.display_details()

print ("_____________________ContractEmployee_________________________")

Emp2.display_details()

for emp in (Emp1, Emp2):
    print(f"{emp.name} ({emp.employee_type}) total salary with bonus: Rs.{emp.calculate_salary()}")