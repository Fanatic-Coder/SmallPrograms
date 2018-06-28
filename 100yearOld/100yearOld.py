fname = input("Enter your first name: ")
lname = input("Enter your last name: ")

yearsstill = int()
yearof100 = int()
yearsago = int()
age = int(input("Enter your age: "))
#I can ask the user to input his birth date and calculate his age

if(age < 100):
    yearsstill = 100 - age  #How many years you got untill you get 100 years old
    yearof100 = 2018 + yearsstill   #What year you ll be closing 100 years old
    print("You are not 100 years old yet. \nYou still got " + str(yearsstill) + " years left!")
    print("You'll be 100 years old at " + str(yearof100) + "!")
elif(age == 100):
    print("You 've just Reached 100 Years old!")
elif(age > 100): #When you are beyond 100 years old
    yearsago = age - 100
    yearof100 = 2018 - 100
    print("Well Done! You 're beyond 100 years old!")
    print("You Closed 100 years old " + str(yearsago) + " years ago! And the year was " + str(yearof100) + "! Have a Long Life!")