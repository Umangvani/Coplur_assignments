from abc import ABC, abstractmethod

class Logger:
    @staticmethod
    def Log(message):
        print(message)

class IEmployee(ABC):
    @abstractmethod
    def CalculateSalary(self):
        pass 
    
    @abstractmethod
    def getDetails(self):
        pass
    
class PermanentEmployee(IEmployee):
    def __init__(self, Name: str, basic_pay: float, bonus: float):
        self.Name = Name
        self.basic_pay = basic_pay
        self.bonus = bonus
            
    def CalculateSalary(self):
        salary = self.basic_pay + self.bonus
        Logger.Log(f"The Salary of the Employee named {self.Name} is {salary}")
        return salary
        
    def getDetails(self):
        return f"Permanent Employee: {self.Name}, Basic Pay: {self.basic_pay}, Bonus: {self.bonus}"
            
class ContractBase(IEmployee):
    def __init__(self, Name: str, hourlyrate: float, hours: int):
        self.Name = Name
        self.hourlyrate = hourlyrate
        self.hours = hours
    
    def CalculateSalary(self):
        salary = self.hourlyrate * self.hours
        Logger.Log(f"The Salary of the Employee named {self.Name} is {salary}")
        return salary
    
    def getDetails(self):
        return f"Contract Employee: {self.Name}, Hourly Rate: {self.hourlyrate}, Hours Worked: {self.hours}"
        
class PayRollGenerate:
    """This class defines the list of all employees and their salary"""
    def __init__(self):
        self.Employee_list = []
            
    def addEmp(self, employee):
        self.Employee_list.append(employee)
        Logger.Log(f"Added employee: {employee.getDetails()}")
            
    def generate_payroll(self):
        Logger.Log(f"Generated Payroll:")
        for employee in self.Employee_list:
            details = employee.getDetails()
            salary = employee.CalculateSalary()
            Logger.Log(f"{details}, Calculated Salary: {salary}\n")
        
if __name__ == "__main__":
    payroll_service = PayRollGenerate()

    # Adding employees
    emp1 = PermanentEmployee(Name="John Doe", basic_pay=5000, bonus=1000)
    emp2 = ContractBase(Name="Jane Smith", hourlyrate=50, hours=160)
    
    payroll_service.addEmp(emp1)
    payroll_service.addEmp(emp2)

    # Generate payroll
    payroll_service.generate_payroll()
