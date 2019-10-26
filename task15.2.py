num = int(input("Enter the number "))
print("The range of the  number: ", num)
print([i**2 for i in range(1,num+1) if i**2 <= num])
