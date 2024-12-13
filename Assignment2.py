#__________________________________________________________________________________________________________
def greet(fname, greeting="Hello"): #creating the function greet with default argument greeting
    print(greeting + " " + fname) #appending greeting and name to print it

#calling functions
greet("Shreya")
greet("Shreya", "Good Morning")

#__________________________________________________________________________________________________________
def create_profile(name, city, age=18): #creating a function create_profile with age as default argument
    print(f'Name: {name}, City: {city}, Age: {age}')

#calling the function with different arguments
create_profile(name="John", city="Chicago")
create_profile(name="Emma", age=22, city="Los Angeles")

#__________________________________________________________________________________________________________
def sum_numbers(*args, **kwargs): #defining a function with both args & kwargs
    sum = 0
    for arg in args:
        sum += arg
    if(len(kwargs) == 0):
        print(f'{sum}')
    else:
        print(f'{sum} {kwargs}')

#calling function with different arguments to see its usage
sum_numbers(1, 2, 3)
sum_numbers(1, 2, x=4, y=5)

#__________________________________________________________________________________________________________
# List of numbers
numbers = [1, 2, 3, 4, 5]
# Use map and lambda to square each element
squared_numbers = list(map(lambda x: x ** 2, numbers))
# Print the squared list
print("Original list:", numbers)
print("Squared list:", squared_numbers)

#__________________________________________________________________________________________________________
def filter_odd_numbers(numbers):
    # Use filter and lambda to filter out odd numbers
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    return even_numbers

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered_list = filter_odd_numbers(numbers)

print("Original list:", numbers)
print("List after filtering odd numbers:", filtered_list)

#__________________________________________________________________________________________________________
# List of numbers
numbers = [1, 2, 3, 4, 5]

# List comprehension to return squares of numbers
squared_numbers = [x ** 2 for x in numbers]

# Print the squared list
print("Original list:", numbers)
print("Squared list:", squared_numbers)

#__________________________________________________________________________________________________________
# List comprehension to generate even numbers between 1 and 20
even_numbers = [x for x in range(1, 21) if x % 2 == 0]

# Print the list of even numbers
print("Even numbers between 1 and 20:", even_numbers)

#__________________________________________________________________________________________________________
import os
import time

def file_operations():
    # Create directory named 'test_folder'
    os.makedirs('test_folder')
    print("Directory 'test_folder' created.")
    
    # Pause the execution for 3 seconds
    time.sleep(3)
    
    # Delete the directory
    os.rmdir('test_folder')
    print("Directory 'test_folder' deleted.")

# Call the function
file_operations()

#__________________________________________________________________________________________________________
# Import only sleep from time module and rename it to pause
from time import sleep as pause

# Pause the execution for 2 seconds
pause(2)

# Print the message
print("Paused execution")

#__________________________________________________________________________________________________________
def flatten_list(*args, **kwargs):
    result = []
    
    # Flatten all positional arguments
    for item in args:
        if isinstance(item, list):  # Check if the item is a list
            result.extend(flatten_list(*item))  # Recursively flatten the nested list
        else:
            result.append(item)  # If not a list, append it to the result

    # Process keyword arguments if any are passed (though lists are usually in *args)
    for key, value in kwargs.items():
        if isinstance(value, list):
            result.extend(flatten_list(*value))  # Recursively flatten nested lists in kwargs
        else:
            result.append(value)
    
    return result

# Example usage
nested_list = [1, [2, [3, 4], 5], 6]
print(flatten_list(nested_list))  # Flattens the nested list
