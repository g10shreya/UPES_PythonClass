# Take an integer input from the user
num = int(input("Enter an integer: "))
# List to hold the number in binary, octal, and hexadecimal formats
equivalents = []
# Loop through to compute binary, octal, and hexadecimal
for base in [2, 8, 16]:
    result = ""
    temp = num
    # Convert the number to the corresponding base using bitwise operations
    while temp > 0:
        remainder = temp & (base - 1)  # Use bitwise AND to compute remainder
        temp = temp >> (3 if base == 8 else 4 if base == 16 else 1)  # Right shift based on base
        # Convert remainder to proper character for hexadecimal if needed
        result = (chr(55 + remainder) if remainder >= 10 else str(remainder)) + result
    equivalents.append(result)

# Print the results
print(f"Binary equivalent of {num}: {equivalents[0]}")
print(f"Octal equivalent of {num}: {equivalents[1]}")
print(f"Hexadecimal equivalent of {num}: {equivalents[2]}")
