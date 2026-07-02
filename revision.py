#if else condition

#buzz number
# num=float(input("enter the number"))
# if(num%7==0 or num%10==7):
#    print("the condition is true")
# else:
#    print("the condition is false")

#to check if the entered year is leap year or not
# num=float(input("enter the year"))
# if(num%4==0 or num%100==0):
#     print("it is a leap year")
# else:
#     print("it is not a leap year")

#to check number entered is prime or not
# num=float(input("enter any number"))
# if (num%2==0 or num%3==0):
#   print("entered number is not prime")
# elif (num%num==0 and num%1==0  ):
#    print("entered number is  prime")

# else:  
#     print("it is composite number")





#to check gender
# char=str(input("select your gender male/female"))
# if(char=="m"):
#     print("you are male")
# else:
#     print("you are female")

#to check if no is positive or negative
# num=float(input("enter the number"))
# if num>0:
#    print("entered no is positive")
# elif num<0:
#    print("entered no is negative")
# else:
#    print("entered no is zero")   

#to find percentage and grade

# eng=int(input("enter your english marks"))
# hindi=int(input("enter your hindi marks"))
# science=int(input("enter your science marks"))
# ss=int(input("enter your sst marks"))
# math=int(input("enter your math marks"))
# per= (eng + math + ss + science + hindi)/5
# print("your Percentage is " , per)
# if per>90:
#     print("you grade is a+")
# elif per>80:    
#     print("you grade is a")
# elif per > 70:
#     print("your grade is b+")
# elif per>60:
#     print("your grade is b")
# elif per>50:
#     print("you grade is c+")
# elif per > 40:
#     print("your grade is c")
# else:
#     print("you are fail")


#fruit name with person 
# x=6
# x>6
# print(not(x>7))



# count=8
# while(count<9):
#     count=count+1
#     print("hello 190")

#print number from 1 to 5
# for i in range(1,6):
#     print(i)

#print even no from 1 to 10
# for i in range(1,11):
#     if(i%2==0):
#         print(i)

#multiplication table of 5 
# for i in range(1,11):
#     print("5*" ,i, "=" ,5*i,) 

#sum of number from 1 to 10
# for i in range(1,11):
#     sum=i*(i+1)/2
# print(sum)

#print a star pattern
# for i in range(1,6):
#     print( "*" * i)

# for i in range (6,1):
    # print("*" * i)

# for i in range (11,1 ,-1):
#     print(i)

# for i in range (10,0,-1):
#     print(i)

#print all odd no from 1 to 20
# for i in range(1,21):
#      if (i%2!=0):
#             print(i)


# for i in range(1,21):
#     if(i%2==0):
#         print(i)

# for i in range(1,11):
#     sum=i*(i+1)/2
# print(sum)

# sum=0

# for i in range(1,11):
#     sum = sum + i
# print(sum)


#multiplication table of 7
# for i in range(1,11):
#     print("7*" ,i,"=" ,7*i,)

# for i in range (5,0 , -1):
#     print("*" * i)
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j, end="")
#     print()


# for i in range(1,6):
#     print("*" *i)

# for i in range(5,0 ,-1)  :  
#     print("*" *i)

# table print
# num=int(input("enter you num="))
# for i in range 

# num1=input("enter you num1=")
# num2=input("enter you num2=")
# num3=input("enter you num3=")
# num4=input("enter you num4=")
# num5=input("enter you num5=")
# list=[num1,num2,num3,num4,num5]
# print(list)

biodata={
    "name":"parul",
    "roll_no":90,
    "marks":80
}
# print(biodata["name"])
# biodata["city"]="delhi"
# biodata["marks"]=90
# print(biodata.keys())
# print(biodata.values())
# del biodata["roll_no"]
#count the  no of items in dict
# print(len(biodata))
# if "marks" in biodata:
#     print("marks is present in biodata")
# else:
#     print("marks is not present in biodata")
# for key , value in biodata.items():
#     print(key,":" ,value) 

# fruit={"apple":90,
#        "orange":89,
#        "banana":78,
#        "grapes":87,
#        "watermelon":85
#      }
# print(fruit["apple"])

# pasport={}
# pasport["name"]=input("enter your name=")
# pasport["age"]=int(input("enter your age"))
# pasport["city"]=input("enter your city")
# print(pasport)

# marks={"english":90,
#         "maths":89,
#         "science":67,
#         "sst":67
# }
# total=sum(marks.values())
# print("total_marks",total)


# marks={"maths":97,
#        "english":78,
#        "hindi":76,
#        "sst":0
# }
# print(max(marks.values()))
# marks={
#     "math":98,
#     "science":89,
#     "sst":97,
#     "french":88
# }
# avg=sum(marks.values())/len(marks)
# print("average marks",avg)

#STORE THE NAMES AND MARKS OF USER FROM INPUT VALUE
# result={}
# for i in range(5):
#     name=input("enter your name:")
#     marks=int(input("enter your marks"))
#     result[name]=marks
# print(result)
#COUNT THE FREQ OF EACH CHAR
# text=input("enter any string:")
# count={}
# for ch in text:
#     if ch in count:
#         count[ch]+=1
#     else:
#         count[ch]=1
# print(count)

#count the freq of each sentence in a word
# sentence=input("enter your sentence:")
# words=sentence.split()
# count={}
# for word in words:
#     if word in count:
#         count[word]+=1
#     else:
#         count[word]=1
# print(count)        

#MERGING TWO DICT
# dict1={
#     "a":90,
#     "b":89
# }
# dict2={
#     "C":76,
#     "d":73
# }
# dict1.update(dict2)
# print(dict1)
#FIND THE TOPER HIGHEST MARKS FROM DICT
# marks={
#     "parul":100,
#     "riya":76,
#     "siya":87,
#     "rahul":56
# }
# topper=max(marks,key=marks.get)
# print("topper:",topper)
# print("marks",marks[topper])





