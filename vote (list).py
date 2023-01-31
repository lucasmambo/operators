eac = ["Kenya", "Uganda", "Tanzania"]
country = str(input("Enter country : "))
age = int(input("Enter Age : "))
if ((age>=18) and (country in eac)):
   print("Eligible to vote")
else:
   print("Not eligible to vote")
