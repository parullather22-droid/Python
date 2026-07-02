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
 
#ARGUMENTS IN FUCNTION
#1 REQUIRED ARGUMENT
# def greeting(name):  #name is parameter
#     print("hello, " + name +"!")
# greeting("parul")   # parul is argument

# def intro(course_name , instructor_name):
#     print("hi," + instructor_name + " this side," +"i will teach you," + course_name)
# intro("python" , "parul")
# TYPES OF FUNCTION ARGUMENTS
# 1 REQUIRED ARGUMENT(SINGLE/MULTIPLE ARGUMENT)
# 2 DEFAULT ARGUMENT
# 3 KEYWORD ARGUMENT(NAMED ARGUMENT)
# 4 ARBITRARY ARGUMENT(VARIABLE LENGTH ARGUMENT)
 



