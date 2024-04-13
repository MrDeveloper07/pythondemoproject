# Define a function to calculate the factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Calculate the factorial of 5
num = 5
print("Factorial of", num, "is", factorial(num))

# Define a list of numbers
numbers = [3, 8, 1, 6, 2, 9, 4]

# Find the maximum number in the list
max_num = max(numbers)
print("The maximum number is:", max_num)
