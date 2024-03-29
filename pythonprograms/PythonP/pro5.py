"""Implement a Python program to find all the numbers divisible by 7 but are not multiple of 5, between 
the range 2000 to 3000. """
# Initialize an empty list to store the numbers
numbers = []

# Iterate through the range from 2000 to 3000
for num in range(2000, 3001):
    # Check if the number is divisible by 7 and not a multiple of 5
    if num % 7 == 0 and num % 5 != 0:
        # Append the number to the list
        numbers.append(num)

# Print the list of numbers
print(numbers)
