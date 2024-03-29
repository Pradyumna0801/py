def count_odd_even(lst):
    odd_count = 0
    even_count = 0
    
    for num in lst:
        if num % 2 == 0:  # Even number
            even_count += 1
        else:  # Odd number
            odd_count += 1
            
    return odd_count, even_count

# Read a list of integer numbers from user input
input_list = input("Enter a list of integer numbers separated by space: ").split()
input_list = [int(num) for num in input_list]  # Convert input strings to integers

# Get the count of odd and even numbers
odd_count, even_count = count_odd_even(input_list)

# Print the counts
print(f"Number of odd numbers: {odd_count}")
print(f"Number of even numbers: {even_count}")
