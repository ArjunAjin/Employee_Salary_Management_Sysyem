from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self,emp_id,name,basic_salary):
        self.emp_id = emp_id
        self.name =name
        self.__basic_salary =basic_salary



    def get_basic_salary(self):
        return self.__basic_salary
    
    @abstractmethod
    def calculate_salary(self):
        pass

    def display_details(self):
        print("Employee ID:",self.emp_id)
        print("Name:",self.name)
        print("Basic Salary:",self.__basic_salary)

    


    