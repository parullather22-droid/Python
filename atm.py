# class student :
#     def __init__(self,name,age):
#         self.name= name
#         self.age= age
# s1=student("parul",9)     
# print(s1.name)
# print(s1.age)

# class student:
#     def __init__(self,name,age):
#        self.name=name
#        self.age=age
#     def display (self):
#         print("name=",self.name)
#         print("age=",self.age)
# s1=student("parul",19)
# s1.display()

# class car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
# c1=car("bmw","m4")   
# c2=car("endeavour","new")
# print(c1.model)
# print(c2.brand)

# class mobile:
#     def __init__(self,company,price):
#         self.company=company
#         self.price=price
#     def display(self):
#         print("phone",self.company)
#         print("price" ,self.price)
# phone1=mobile("iphone",100000)
# phone2=mobile("vivo",8000)
# phone2.display()
# phone1.display()
# class Book:
#     def __init__(self,title ,author):
#         self.title=title
#         self.author=author
#     def display (self):
#             print("title", self.title)
#             print("author",self.author)

# title1=input("enter your book title1:")  
# author1=input("enter your book author1:")          
# title2=input("enter your book tite 2 :")
# author2=input("enter your book author2:")  

# book1=Book(title1,author1)
# book2=Book(title2,author2)

# book1.display()
# book2.display()

# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth 
#     def area(self) :
#         return self.length * self.breadth
# r1=Rectangle(90,89)
# print("area=",r1.area())
  
#LEVEL 2  
# class Employee:
#     def __init__(self,name ,salary):
#         self.name=name
#         self.salary=salary
# e1=Employee("parul",100000)
# print(e1.name)
# print(e1.salary)

# class Circle:
#     def __init__(self,radius):
#         self.radius=radius   
#         pie=3.14
#         self.area=3.14*radius*radius

# radius=int(input("enter any number")) 
# c1=Circle(radius)
# print("area",c1.area)

# class laptop:
#     def __init__(self,brand,RAM,SSD):
#         self.brand=brand
#         self.RAM=RAM
#         self.SSD=SSD
# laptop1=laptop("lenovo",16,256) 
# print("brand:",laptop1.brand)
# print("RAM:",laptop1.RAM)
# print("SSD:",laptop1.SSD)

# class bank:
#     def __init__(self,account_holder,balance):
#         self.account_holder=account_holder
#         self.balance=balance

# person1=bank("parul",100000000)
# print("balance:",person1.balance)

# class movie:
#     def __init__(self,movie_name,rating):
#         self.movie_name=movie_name
#         self.rating=rating
# movie1=movie("off campus",10)
# print("movie:",movie1.movie_name)
# print("rating:",movie1.rating)

# class calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         return self.a + self.b 
#     def sub(self):
#         return self.a-self.b
#     def multi(self):
#         return self.a *self.b
#     def  div(self):
#         if self.b !=0:
#             return self.a*self.b
#         else:
#             return ("divison by zero is not possible")
        
# num1=int(input("enter your num1:"))
# num2=int(input("enter your num2:"))
# c=calculator(num1,num2)
# print("addition=",c.add())
# print("substraction=",c.sub())
# print("multiplication=",c.multi())
# print("divison=",c.div())

# class temprature:
#     def __init__(self,celsius ,fahrenheit):
#         self.celsius=celsius
#         self.fahrenheit=fahrenheit

#     def celsius_to_fahrenheit(self):
#        return  (self.celsius*9/5)+32
    
#     def fahrenheit_to_celsius(self):
#             return (self.fahrenheit -32)*5/9
# c=int(input("enter your temprature in celsius"))
# f=int(input("enter your num in faherenit"))
# t=temprature(c,f)
# print("celsius_to_faherenit=",t.celsius_to_fahrenheit())
# print("fahrenheit_to_celsius=",t.fahrenheit_to_celsius())

# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def speak (self):
#         print(f"{self.name}makes a sound")
# class Cat(Animal):
#     def speak(self):
#         print(f"{self.name} says Meow!")
# Cat("niya").speak()

#BASIC CLASS + ENCAPSULATION
# class BankAccount:
#     def __init__(self, owner ,balance=0):
#         self.owner=owner 
#         self.__balance=balance  #double underscore - private attribute
#     def deposit(self,amount):
#         if amount<=0:
#             print("deposit must be positive")
#             return
#         self.__balance=+amount
#         print(f"deposited {amount}.new balance{self.__balance}")
#     def withdraw(self,amount):
#       if amount  >self.__balance:
#           print("insufficient balance")
#           return
#       self.__balance-=amount
#     def get_balance(self):
#         return self.__balance

# acc=BankAccount("alia",1000)      
# acc.withdraw(2000)
# acc.deposit(1000)
# print(acc.get_balance())

#INHERITANCE-EMPLOYEE HIERARCHY
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
        # self.salary=salary

#     def show_deatils(self):
#         print(f"Name:{self.name}, Salary:{self.salary}")  

# class Manager(Employee):
#     def __init__(self, name, salary,team_size):
#         super().__init__(name, salary)
#         self.team_size=team_size

#     def show_details(self):
#         super.show_deatils()
#         print(f"Manager a team of {self.team_size}")
# e=Employee("Priya",5000)
# m=Manager("Arya",50000,5)
# e.show_deatils()
# m.show_deatils()

class Shape:
    def area(self):
          print("this is shape class")
        #   raise NotImplementedError("subclass must implent this")
class Rectangle(Shape):
     def __init__(self,w,h):
          self.w =w
          self.h=h
     def area (self):
          return self.w*self.h
     
class Circle(Shape):
     def __init__(self,r):
               self.r=r
     def area(self):
                return 3.14*self.r*self.r
shapes = [Rectangle(4, 5),Circle(3), Rectangle(2, 2)]

for s in shapes:
    print(f"{type(s).__name__} area: {s.area():.2f}")        

# class Student:
#     def __init__(self,m1,m2,m3,m4,m5):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
#         self.m4=m4
#         self.m5=m5
#         def total(self):
#             return self.m1 + self.m2 + self.m3 + self.m4 + self.m5
#         def percentage(self):
#             return self.total()/5    
    
# m1=int(input("enter your marks of sub1="))
# m2=int(input("enter your marks of sub2="))
# m3=int(input("enter your marks of sub3="))
# m4=int(input("enter your marks of sub4="))
# m5=int(input("enter your marks of sub5="))
# student=Student(m1,m2,m3,m4,m5)
# print("total marks=",student.total())
# print("percentage=",student.percentage(),"%")