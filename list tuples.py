#list=a built in data type s that stores value it can be int,float ,str

# marks=[97.9,89.9,78.9,78.7,56.7]
# # print(marks)
# # print(type(marks))
# # print(marks[4])
# print(len(marks))

#ham 1 hi list mei diff types ka data store kr skte h jaise ki int float str sab 1 sath ho skta h
# student=["parul",22, "girl" , "december"]
# print(student[0])

#strings h vo immutable hote h we cant chnge them 
#list mutable hoti h we can chnge them
# str="hello"
# print(str)
# str[0]="y" # asa krege toh error ayga bcz we cant chnge strng

# student=["parul",22, "girl" , "december"]
# print(student[0])
# student[0]="age" #isme koi error nhi ayga ab aage new list primt kra skte h
# print(student)#new list m chnged value aajygi
 
#LIST SLICING same as str slicing last indx is not included
# marks=[89,77,78,60,56,69,67]#indx 0 se shuru hota h
# print(mark,s[1:6])#1 se 6 ka mtlb h se 1 se 5 vali sab value aygi
# print(marks[1:])#ye last nhi ikha toh automtaiclly last tk jyga
# print(marks[:4])#agr shuru vala nhi likha toh automatic 0 se strt hoga
# print(marks[-3:-1])

#LIST METHOD
# list=[2,1,3]
# list.append(4)#add one elements to end (2,1,3,4)
#list.extend([])#isme hm list k andr or values add kr skte h
# list.sort()#sorts in ascending order(1,2,3)
# list.sort(reverse=True)# sort sin descending order (3,2,1)
# list.reverse() #reverses list (3,1,2)
# list.insert#(idx,el) inssert element at index
# list.remove(1)#jo bhi remove krna h usko bracket m likho agr 1 cheez 2 bar h toh phle vala hatega
# list.pop(1)#remove element from index ab ye 1 pr sse 1 ko remove rkega
#list.clear()# isse sab elemnets clear hojayege
# numbers=[5,9,8,5]
# # print(max(numbers))
# print(min(numbers))
#TUPLES
# tup=(1,2,3,4)
# print(tup)
# # print(tup[0])
# tup[0]="y"#isme value chnge nhi hoe
# tup=()
# print(tup)#empty tuple bhi print krwa skte h
# print(type(tup))
#AGAR HAME SINGLE INT KO TUPLE M LIKHNA H TOH USKO ASA LIKEHGE
# tup=(1,)# ham comma lagayega agr coma nhi lagayga toh vo usko int smjhega
# print(tup)
#tuples k andr bhi slicing hoti h
# tup=(1,2,3,4,5)
# print(tup[1:4])#(2,3,4)

#TUPLE METHOD
# tup=(1,2,3,4,2,2)
# # print(tup.index(2))#ye isme element 2 ka index btyga 
# print(tup.count(2))#ye hame ye batayaga ye element kitne bar aya h
# a=str(input("enter you movie a:"))
# b=str(input("enter you movie b:"))
# c=str(input("enter you movie c:"))
# movie=[a,b,c]
# print(movie)"
# tup=["C","D","B","A","A","B","A"]
# # print(tup.count("A"))
# print(tup)
# tup.sort()
# print(tup)

# fruits=["apple","orange","banana","peach","watermelon"]
# fruits.append("mango")
# print(fruits)




