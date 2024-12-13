# Taking three number inputs from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Calculating the average
average = (num1 + num2 + num3) / 3

# Printing the average using the % method for string formatting
print("The average of three numbers is: %.2f" % average)
