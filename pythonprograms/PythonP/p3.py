""" Implement a Python program to read two list and display common elements of the given lists"""

def find_common_elements(list1, list2):
    # Convert lists to sets
    set1 = set(list1)
    set2 = set(list2)
    
    # Find intersection of the two sets
    common_elements = set1.intersection(set2)
    
    return list(common_elements)

# Read two lists from user input
list1 = input("Enter elements of the first list separated by space: ").split()
list2 = input("Enter elements of the second list separated by space: ").split()

# Display common elements
common_elements = find_common_elements(list1, list2)
print("Common elements of the given lists:", common_elements)
