a = 10
b = 5

#trying out various operators
if a > b and b > 0:
    print("Both conditions are true.")

if a != b:  # Not equal to
    print("a is not equal to b")

if a > b:   # Greater than
    print("a is greater than b")

if a < b:   # Less than
    print("a is lesser than b")

if a >= b:  # Greater than or equal to
    print("a is greater or equal to b")

if a <= b:  # Less than or equal to
    print("a is lesser or equal to b")

#seeing the working of bitwise operators
a = 6  # (in binary: 110)
b = 3  # (in binary: 011)
print(a & b)  # Bitwise AND
print(a | b)  # Bitwise OR
print(a ^ b)  # Bitwise XOR
print(~a)     # Bitwise NOT
print(a << 1) # Left shift
print(a >> 1) # Right shift

#looking at the working of a while loop & break statement
count = 2
while count < 10:
    if count == 5:
        break
    print(count)
    count += 1

#looking at the working of a while loop & continue statement
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)

#trying out for loop
for i in range(5):
    print(i)

for i in range(0, 10):
    print(i)

