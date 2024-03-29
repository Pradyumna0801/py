""" Implement a python program which will read a list of integer numbers. Then it will create a dictionary 
which contains the key: value pair as: key is N and value is the number of negative numbers and the 
second key is P and the value is the number of positive numbers contained in list. (for example List=[ 
9,-3,4,8,-17] the output will be Dlist={ ‘N’:2, ‘P’:3})
"""
def count_numbers(numbers):
    positive_count = 0
    negative_count = 0
    
    # Iterate through the list of numbers
    for num in numbers:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
            
    # Create and return the dictionary
    count_dict = {'P': positive_count, 'N': negative_count}
    return count_dict

# Read a list of integer numbers from user input
input_list = input("Enter a list of integer numbers separated by space: ").split()
input_list = [int(num) for num in input_list]  # Convert input strings to integers

# Get the count of positive and negative numbers
result_dict = count_numbers(input_list)

# Print the result dictionary
print("Result Dictionary:", result_dict)
