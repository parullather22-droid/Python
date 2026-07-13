#1 -STUDENT CLASS
# class Student:
#     def __init__(self, name,age):
#         self.name=name 
#         self.age=age

#     def display (self):
#         print("name",self.name)
#         print("age", self.age)
# s1=Student("parul",18)
# s1.display()

#2 - RECTANGLE
# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth

#     def area(self):
#         print("Area=", self.length *self.breadth)

# r1=Rectangle(10,5)
# r1.area()

#3=EMPLOYEE CLASS
# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary

#     def display(self):
#         print("employee name=" , self.name)
#         print("salary=",self.salary)

# E1=Employee("pari",10000)
# E1.display()

#4=CIRCLE AREA
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius

#     def area(self):
#         area=3.14*self.radius*self.radius
#         print("area=",area)
# c1=Circle(9)
# c1.area()      

#5=BANK ACCOUNT
# class BankAccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
#     def display(self):
#         print("account holder=",self.name)
#         print("balance=",self.balance)
# account=BankAccount("Parul",1000000)
# account.display()
    
#6=CALCULATOR
class Calculator:
    def add(self, a, b):
        print("Addition =", a + b)

    def subtract(self, a, b):
        print("Subtraction =", a - b)

    def multiply(self, a, b):
        print("Multiplication =", a * b)

    def divide(self, a, b):
        print("Division =", a / b)

c = Calculator()

c.add(10, 5)
c.subtract(10, 5)
c.multiply(10, 5)
c.divide(10, 5)