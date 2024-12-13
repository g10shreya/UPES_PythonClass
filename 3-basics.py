#seeing how to create a function in python
def calculate_average(marks):
    total = sum(marks)
    return total / len(marks)

# Taking input scores
user_name = input("Enter Student's Name: ")
num = int(input("Enter the number of subjects: "))

#declaring an array to enter marks
marks = []

#using loop to enter marks
for i in range (num):
    ele = int(input(f"Enter the marks of subject {i+1}: "))
    marks.append(ele)  

#calling our function and passing arguments in it
average = calculate_average(marks) 

print("The average of marks is: ", average)

