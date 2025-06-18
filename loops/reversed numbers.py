n = int(input("Enter the range of numbers: "))
print("Even Numbers: ")
for i in  range(2,n+1,2):
    print(i)
print("Odd Numbers: ")
for i in  range(1,n+1,2):
    print(i)

print("Reversed Numbers: ")
for i in  range(n, 0, -1):
    print(i)



