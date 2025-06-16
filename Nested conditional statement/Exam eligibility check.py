medical_cause = input("Did you have any medical issue (y/n): ")
attendence = int(input("Enter the persentage of attention: "))
if medical_cause == 'y' :
     print("Allowed")
else:
     if attendence < 75:
          print("Not allowed")
     else:
         print("Allowed")
    