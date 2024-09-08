# Define the lambda functions

 

double = lambda x: x * 2

 

add = lambda x, y: x + y

 

# Take input from the user

 

num = int(input("Enter a number: "))

 

num1 = int(input("Enter first number: "))

 

num2 = int(input("Enter second number: "))

 

# Apply the lambda functions

 

result1 = double(num)

 

result2 = add(num1, num2)

 

# Display the results

 

print("Double of", num, "is", result1)

 

print("Sum of", num1, "and", num2, "is", result2)