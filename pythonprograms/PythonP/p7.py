""" Implement a python program to demonstrate the concept of set data structure."""
# Create a set
my_set = {1, 2, 3, 4, 5}
print("Initial Set:", my_set)

# Adding elements to a set
my_set.add(6)
my_set.add(7)
print("Set after adding elements:", my_set)

# Removing elements from a set
my_set.remove(3)
print("Set after removing 3:", my_set)

# Checking membership in a set
print("Is 5 in the set?", 5 in my_set)
print("Is 10 in the set?", 10 in my_set)

# Length of a set
print("Length of the set:", len(my_set))

# Iterating through a set
print("Iterating through the set:")
for item in my_set:
    print(item)

# Creating a set from a list (removes duplicates)
my_list = [1, 2, 3, 4, 4, 5, 5]
unique_set = set(my_list)
print("Set from list:", unique_set)

# Set operations: union, intersection, difference
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
print("Union:", set1.union(set2))

# Intersection
print("Intersection:", set1.intersection(set2))

# Difference
print("Difference (set1 - set2):", set1.difference(set2))
print("Difference (set2 - set1):", set2.difference(set1))
