n = int(input("enter the no. numbers you want to sum: "))
sum = 0 
for i in range(n+1):
    sum = sum + i
    print("Sum:", sum)
print("Total sum: ", sum)