#FUNCTION-a function is a block of reusable codes that performs a specific task 
#create function:use the def keyword to define a function
#call function : use the function name followed by ()
#parameter : the varaible listed under paranthesis in the fucntion def
#argument: the actual value you pass to function when you call it 
#TYPES OF FUNCTION
#1=built in function 2 = user defined function

# SYNTAX OF FUCNTION
# def my_functiom(param):
#     instruction-1
#     instruction=2
#     return result

#EXAMPLES
#CREATE OR DEFINE FUNCTI0NS
#1. def greeting():
#     print("helo welocme to my you tube")
# #USE OR CALL THIS FUNCTIONS
# greeting()
# #OUTPUT : HELLO WELCOME TO MY YOUTUBE

#functions with parameter
#functions to add 2 number and print result
# def add2number(a,b):
#     result=a+b
#     print("the sum is:" , result)
# # add2number(5,3)
# add2number(a=10,b=90)

#functions to add 3 number and print resulut
# def addnumber(a,b,c):
#     result=a+b+c
#     print("the sum is :",result)

# def addnumber(a,b,c):
#     if c!=0:
#         print(a+b+c)
#     else:
#         print(a+b)  
# a=int(input("enter your num1="))
# b=int(input("enter your num2="))
# c=int(input("enter your num3(0 if not needed)="))

# addnumber(a,b,c)


# addnumber(90,87,76)
# function with return statement
# def add2num(a,b):
#     return a+b
#     #return a-b # after return statement function ends
# sum2num = add2num(9,787)
# print(sum2num)


# #FUNCTIONS WITH PARAMETER
# # def greet(name):
#     print("hello" , name)
# greet("parul")    

# def square(x):
#     return(x*x)
# print(square(4))

# def even_odd(n):
#     if n%2==0:
#        print ("even")
#     else:
#         print("odd")
# even_odd(14)

#function to convert celsius to fahernenit with return 
# def celsius_to_faherenit(celsius):
#     faherenit=( celsius *9/5 )+32
#     return(faherenit)
# temp_f = celsius_to_faherenit(25)
# print("the temprature in faherenit is :", temp_f)
# print(type(temp_f)) # isme clasws float ayyaga

#FUNCTION TO CONVERT CELSIUS TO FAHRENIT WITHOUT RETURN ONLY PRINT
# def celsius_to_faherenit(celsius):
#     faherenit=( celsius *9/5 )+32
#     print(faherenit)
# temp_f2=celsius_to_faherenit(25)
# print(type(temp_f2))   #isme class none type aygga
 
#THE PASS STATEMENT
#the pass statemnet is a placeholder in a function or loop. it does nothing and is used when you need to write code that will be added later  or to define an empty function
# example: def myfunction():
# pass # this does nothing to a function
# def kuchbhi():
#     pass
# print("hello")
# TYPES OF FUNCTION ARGUMENTS
#ARGUMENTS IN FUCNTION
# 1 REQUIRED ARGUMENT(SINGLE/MULTIPLE ARGUMENT)
# def greeting(name):  #name is parameter
#     print("hello, " + name +"!")
# greeting("parul")   # parul is argument

# def intro(course_name , instructor_name):
#     print("hi," + instructor_name + " this side," +"i will teach you," + course_name)
# intro("python" , "parul")

# 2 DEFAULT ARGUMENT  = isme default value asign hoti h
# def greeting(name="parul"):
#     print("hello ," + name + "!")
# greeting()
# 3 KEYWORD ARGUMENT(NAMED ARGUMENT)
# when calling a function you can specify arguments by parameter name
# def divide(a,b):
#     return a/b
# result=divide(90,9)
# print(result)

# 4 ARBITRARY ARGUMENT(VARIABLE LENGTH ARGUMENT)
# if you are unsure how many arguments will be pased use *args to accept any number of positional argumnets
#arguments are stored as a tuple
# def add_numbers(*args):
#     return sum(args)
# result=add_numbers(5,8,8,844,78)
# print(result)

# def greetings2(*names):
#     for name in names:
#         print(f"hello,{name}!")
# greetings2("parul","anushka")

# def print_details(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}:{value}")
# print_details(name="parul", age=90, course="btech")     
   
# def series(n):
#     for a in range(1, 11):
#         print(n ** a)

# series(5)

# num1=int(input("enter your num1="))
# num2=int(input("enter your num2="))

# print("choose your operators below")
# print("1. your opertaor is addition")
# print("2. your opertaor is substraction")
# print("3. your opertaor is multiplication")
# print("4. your opertaor is division")
# choice=int(input("enter you choice"))

# if choice==1:
#     print("Addition",num1+num2)
# elif choice==2:
#     print("Substarction",num1-num2)
# elif choice==3:
#     print("multiplication",num1*num2)
# elif choice==4:
#     if num2 !=0:
#         print("division", num1/num2)
#     else: 
#         print("Error : cannot divisble by 0.")
# else:
#     print("Invalid input. please select any one 1,2,3,4")

#CALCULATOR USING FUNCTIONS
# a=int(input("enter your a="))
# b=int(input("enter your b="))
# def addition(a,b):
#     return a+b
# def substraction(a,b):
#     return a-b
# def multiplication(a,b):
#     return a*b
# def division(a,b):
#         return a/b
# choice=int(input("enter you choice"))
# if choice==1:   
# #     print(addition(a,b))

# elif choice==2:
#     print(substraction(a,b))

# elif choice==3:
#     print(multiplication(a,b))

# elif choice==4:
#     if b!=0:
#      print(division(a,b))
#     else:
#         print("cannot divisble")
# else:
#     print("you have selected wrong chocie")