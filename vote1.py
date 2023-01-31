citizen = (input("Are you a Kenyan Citizen (yes/no) : "))
age = int(input("Enter age : "))
if ((citizen == "yes") and (age>=18)):
   print("Eligible to vote")
else:
   print("Not eligible to vote")
