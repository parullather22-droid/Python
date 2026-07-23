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
# class Calculator:
#     def add(self, a, b):
#         print("Addition =", a + b)

#     def subtract(self, a, b):
#         print("Subtraction =", a - b)

#     def multiply(self, a, b):
#         print("Multiplication =", a * b)

#     def divide(self, a, b):
#         print("Division =", a / b)

# c = Calculator()

# c.add(10, 5)
# c.subtract(10, 5)
# c.multiply(10, 5)
# c.divide(10, 5)

#7=INHERITANCE
# class animal:
#     def sound(self):
#         print("animal makes a sound")
# class dog (animal):
#     def bark(self):
#         print("dog barks")
# d=dog()
# d.sound()
# d.bark()

# class Student:
#     def __init__(self,name,roll_no,marks):
#         self.name=name
#         self.roll_no=roll_no
#         self.marks=marks
#     def percentage(self):

#         return self.marks

#     def grade(self):
#         if self.marks>=90:
#             return "A+"
#         elif self.marks >=80:
#             return "A"
#         elif self.marks>=70:
#             return "B+"
#         elif self.marks >=60:
#             return "B"
#         elif self.marks>=50:
#             return "C+"
#         else:
#             return "Fail"

#     def display (self):
#         print("------Student Report-------")
#         print("Name:" ,         self.name)
#         print("Roll No:",       self.roll_no)
#         print("Marks: ",        self.marks)        
#         print("Percentage:",    self.percentage(),"%")
#         print("Grade:",         self.grade())

# name=input("enter your name:")
# roll=int(input("enter your roll no:"))
# marks=float(input("Enter Marks(out of 100):"))

# student1=Student(name,roll,marks)
# student1.display()

class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def deposit(self):
        amount=int(input("enter the amount you want to deposit="))    
        self.balance=+amount
        print("amount deposited succesful")
        print("Your new balance is",self.balance)
        

    def withdraw(self,amount):
         self.balance=9000
        amount=int(input("enter the amount="))
        if amount<=self.balance:
            print("withdrawn succesfull")
            self.balance-=amount
            print("your new balance is",self.balance)
        else:
            print("Insufficent balance")
       

    def check_balance(self):
        current_balance=9000
        print("Your current_nalance is ",self.balance)
print("choose the service")
print("1.deposit")
print("2.withdraw")
print("3.check balance")
choice=int(input("enter your choice"))        

account=BankAccount("parul",9000)
account.withdraw(1000)
account.check_balance()
account.deposit(1000)