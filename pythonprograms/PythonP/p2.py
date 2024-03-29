""" Implement a Python program to demonstrate the concept of multiple inheritance."""

# Parent class 1
class ParentClass1:
    def method1(self):
        print("Method from ParentClass1")

# Parent class 2
class ParentClass2:
    def method2(self):
        print("Method from ParentClass2")

# Child class inheriting from ParentClass1 and ParentClass2
class ChildClass(ParentClass1, ParentClass2):
    def method3(self):
        print("Method from ChildClass")

# Create an object of ChildClass
obj = ChildClass()

# Calling methods
obj.method1()  # Method from ParentClass1
obj.method2()  # Method from ParentClass2
obj.method3()  # Method from ChildClass
