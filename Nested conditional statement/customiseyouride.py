print("select your ride: ")
print("1.Bike")
print("2.Car")
#take input number 1 or 2
#select your ride
choice = int(input("Enter your choice: "))

#User entering option 1
if( choice == 1 ): #condition 1 outer if statement
    print("what type of bike? ")
    print("1.Scooty\n")
    print("1.Scooter\n")

#Condition for selection for the type of bike
choice2=int(input("enter your choice2: "))
if choice2==1: #inner if statement
    print("You have selected scooty")
else:
    print("You have selected scooter")
#User entering option 2 

 elif   ( choice == 2 ) :  #outer  elif  statement 
print( "What type of car?" )
     print("1.Sedan")
     print("2.XuV")
     choice3=int(input("enter your choice3: "))
  
     if  choice3==1 #inner if statement 
     #condition for selecting the type of car
     print("You have selected Seden")
     else:
     print("You have selected XUV")
else:
    print("Wrong choice!")
  