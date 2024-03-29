"""Implement a Python program to find all prime numbers between 100 and 500."""
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Find prime numbers between 100 and 500
prime_numbers = [num for num in range(100, 501) if is_prime(num)]

# Print prime numbers
print("Prime numbers between 100 and 500:")
print(prime_numbers)
