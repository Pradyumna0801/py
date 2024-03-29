""" Implement a Python program to sort an inputted list using insertion sort."""
def insertion_sort(arr):
    # Traverse through the list
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Read a list of numbers from user input
input_list = input("Enter a list of numbers separated by space: ").split()
input_list = [int(num) for num in input_list]  # Convert input strings to integers

# Sort the list using insertion sort
insertion_sort(input_list)

# Print the sorted list
print("Sorted list:", input_list)
