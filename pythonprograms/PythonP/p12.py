def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def count_leap_years(years):
    leap_count = 0
    for year in years:
        if is_leap_year(year):
            leap_count += 1
    return leap_count

# Read a list of integer years from user input
input_years = input("Enter a list of years separated by space: ").split()
input_years = [int(year) for year in input_years]  # Convert input strings to integers

# Get the count of leap years
leap_count = count_leap_years(input_years)

# Print the count of leap years
print(f"Number of leap years: {leap_count}")
