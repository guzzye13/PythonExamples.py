# Python Object-Oriented Programming
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('Corey', 'Scaher', 50000)
emp2 = Employee('Test', 'User', 60000)

print(emp1.email)
print(emp2.email)
print(emp1.fullname())