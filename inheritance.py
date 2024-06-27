class Employee:
    def __init__(self, name, lastname, pay, empid, dept):
        self.name = name
        self.lastname = lastname
        self.pay = pay
        self.empId = empid
        self.dept = dept

    def getEmpEmail(self):
        return self.name + '.' + self.lastname + '@chotuferm.com'

    def raise_pay(self,raiseAmt):
        self.pay= self.pay * raiseAmt

class Developer(Employee):
    def __init__(self, name, lastname, pay, empid, dept, prog_lang ):
        super().__init__(name, lastname, pay, empid, dept)
        self.prog_lang=prog_lang

emp1=Employee("garv","mehra",99000,"cs01","frontend")
emp2=Employee("Vivek","mehra",172000,"cs09","backend")
emp3=Developer("Prashant","mehra",339000,"cs019","frontend_backend","python")

print(emp1.pay)
print(emp2.getEmpEmail())
emp3.raise_pay(1.04)
print(emp3.pay)
