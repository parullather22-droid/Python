print("welcome to bank of india")
print("Below are the serivces we provide:")
print("1.check your account balance\n2.withdrawal cash\n3.Deposit amount\n4.Open new account")

option= int(input("enter your choice="))
balance=60000

if option == 1 :
   print("Your account balance is: ",balance)

elif option == 2:
  amount = int(input("Enter your withdrawl amount ="))
  new_balance = balance - amount
  print("Your updated balance is",new_balance)

elif option ==3:
   amount = int(input("Enter your deposit amount= "))
   new_balance = balance + amount
   print("Your updated balance is",new_balance)


elif option == 4: 
   print("Please enter the below details to open new account:")
   name= input("Enter your name=")
   adhar_no = int(input("Enter adhar number="))
   email = input("Enter your email=")   
   mobile=int(input("Enter your mobile number="))
   Pan_No= input("Enter your Pan number=")
   choice = input("Are you sure to submit your details for opening new account? Yes/No").lower()

   if choice == 'yes':
      print("Please check your details")
      print("Your name is",name)
      print("Your adhar number is",adhar_no)
      print("Your email is",email)
      print("Your mobile number is",mobile)
      print("Your Pan number is",Pan_No)
   else:
      print("Thank you for giving the confirmation")  


else:
   print("invalid option ")