#to map real world scenarios we started using obejcts in code . to inc reusability we use oops
#CLASS AND OBJECT IN PYTHON
# class is a blueprint for creating objects 
# eg class Student: class name is like as variable name and strt with capital letter
#     name="parul"
# # creating object(instances)

# #student details
# # student_1=['parul',10]
# # student_2=['arya',90]
# # print(f'{student_1[0] } is in class {student_1[1]}')
# # print(f'{student_2[0] } is in class {student_2[1]}')
# #this is very long method and cant be used for many variables 

#  #why oops?
#  #real world problem, code reusability ,easier maintanence, encapsulation(protect data, privacy)
#  #using oops
#  #class - blueprint or template 
# class Student:
#     def __init__(self,name,grade,percentage,team):  # self= class object k beech m relation k liye
#         self.name= name  
#         self.grade= grade  #attribute
#         self.percentage= percentage
#         self.team=team

    # def student_details(self):
    #     print(f"{self.name} is in class {self.grade} with {self.percentage} percent")
       
# team1='A'  # class ko object se link kia h
# team2='B'
# object- instance of class
# student1=Student('parul',10,99,team1)
# print(student1.name,student1.grade)

# student2=Student('arya' ,12,78,team2)
# print(student2.name,student2.grade)

# print(student1.team)
# print(student1.percenatage)
# student2.student_details()

# print(student1.__dict__)  # iss se key value pair ki form m print hoga

#MODIFIED OBJECT PROPERTY

# print(student1.percentage)
# student1.percentage=90
# print(student1.percentage)

#DELETE OBJECT PROPERTY
# print(student1.__dict__)
# del student1.grade
# print(student1.__dict__)

# #DELETE OBJECT
# del student1
# print(student1)  # ab error ayga bcz delete hogya h

# 4 FEATURES OF OOPS
#Abstraction
#Encapsulation
#Inheritence
#Polymorphism

#ABSTRACTION-hiding unneccasry details from users through class ,methods
class Student:
    def __init__(self,name,grade,percentage,team): 
        self.name= name  
        self.grade= grade  
        self.percentage= percentage
        self.team=team

    def student_details(self):
        print(f"{self.name} is in class {self.grade} with {self.percentage} percent")
 #object- instance of class
student1=Student('parul',10,99,)
student2=Student('arya',12,99)

print(student1.percentage)
# student1.student_details()
