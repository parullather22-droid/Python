#to map real world scenarios we started using obejcts in code . to inc reusability we use oops
#CLASS AND OBJECT IN PYTHON
# class is a blueprint for creating objects 
# eg class Student: class name is like as variable name and strt with capital letter
#     name="parul"
# creating object(instances)

# class Student:
#     name="parul"
# s1=Student()
# print(s1)
# print(s1.name)
# s2=Student()
# print(s2.name)

# class Car:#class
#     colour="blue"
#     brand="bmw"
# car1=Car() # object
# print(car1.colour)
# print(car1.brand)

#_ _init_ _ function = all clasees have a function called init() which is always executeed when the class is being initiated
#creating class                                    #creating object
# class Student:                                       s1=Student("parul")
#     def __init__(self,fullname):                   print(s1.name) 
#     self.name =fullname
# #the self paramter is used to refrecence to the current instances of class and is used to access variable that belongs to object
class Students():
    name="parul"
    def __init__(self):
        print("adding new students")
        

       