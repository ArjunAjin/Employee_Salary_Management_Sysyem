from Employee import Employee

class PermanentEmployee(Employee):
    employee_type = "permenent"
    
    def calculate_salary(self):
        return self.get_basic_salary() + self.get_basic_salary() * 0.2

    
    