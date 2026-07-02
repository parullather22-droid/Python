#DICTIONARY
# info={
#     "name":"parul",
#     "subjects":["python","jaava","c+"],
#     "topics":("dictionary","set"),
#     "college":"bml",
#     "age":19,
#     "is_adult":"true"
# }

# # print(type(info))
# info["name"]="arya"#asa krne se new add hota h
# info["surname"]="lather"#asa add bhi hojata h
# print(info)

#PROPERTY
#dictoaniers are used to store value in key:value pairs
#they are unordered,mutable(unchangble),dont allow duplicate keys

# null_list={
# }
# null_list["name"]="parul"
# print(null_list)
#NESTED DICTIONARY
# student={"name":"parul",
#          "subjects":{"maths":90,
#                      "science":62,
#                      "eng":52,
#                      }
# }
# print(student["subjects"]["maths"])
#DICTIONARY METHOD
# myDict.keys()#returns all keys
# myDict.values()#return all values
# myDict.items()#return all (keys:values)pair in tuples
# myDict.update(new dict)#insert the specified item to dict
# myDict.get("key"") # return the key acc to value
# student={"name":"parul",
#          "age":80,
#          "subjects":{"maths":90,
#                      "science":62,
#                      "eng":52,
#                      }
# }
# print(student.keys())#isse key print hogi name ans sub nested vali key nhi aati
# # print(student.values())#isme values print hogi
# # print(student.items())
# # print(len(student))#isse jo no of keys h vo pata chlega
# # print(len(student.keys()))

# print(student)
# prices={
#     "apple":90.9,
#     "orange":89.6,
#     "banana":55.4
# }
# # print(prices["apple"])
# for fruit,prices in prices . items():
#     print(f"{fruit}:${prices}")

student={
    "name":"parul",
    "course":"btech",
    "age":90
}
# student["age"]="99"
# del student["name"]
# print(student.keys())
# print(student.values())
# for key, value in student.items():
#     print(key, ":", value)
#count frequency of char 
# word="apple"
# count={}
# for ch in word:
#     if ch in count:
#         count[ch]+=1
#     else:
#         count[ch]=1
# print(count)
#student marks 
# marks={
#     "math":99,
#     "science": 89,
#     "sst":87
# }
# total= sum(marks.values())
# print(" total marks=", total)
#TAKE INPUT FROM USER
# student={}
# student["name"]=input("enter your name=")
# student["age"]=input("enter your age=")
# student["grade"]=input("enter your grade=")
# print(student)

