""" Implement a python program which read integer numbers form user and create a list. Then check every 
number in list is odd or even. Then replace odd numbers by 0 and even numbers by 1. (for example, 
for input L1= [ 2,6,7,19,8] then output will be L1= [1,1,0,0,1])"""
def check_and_replace_numbers(lst):
    for i in range(len(lst)):
        if lst[i] % 2 == 0:  # Even number
            lst[i] = 1
        else:  # Odd number
            lst[i] = 0

# Read a list of integer numbers from user input
input_list = input("Enter a list of integer numbers separated by space: ").split()
input_list = [int(num) for num in input_list]  # Convert input strings to integers

# Check and replace numbers in the list
check_and_replace_numbers(input_list)

# Print the result list
print("Result List:", input_list)
