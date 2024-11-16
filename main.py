
def add_numbers(a, b):
    # Adding two numbers and returning the result
    result = a + b
    return result

sum_result = add_numbers(3, 5)
print("The sum of 3 and 5 is:", sum_result)

def multiply_numbers(x, y):
    product = x * y
    return product
product_result = multiply_numbers(4, 6)
print("The product of 4 and 6 is:", product_result)

def greet(name="Guest"):
    print(f"Hello, {name}! Welcome to Python.")

# Calling the function without any arguments uses the default parameter.
greet()

# Calling the function with a specific name.
greet("Alice")

# Function with Multiple Return Values
# A function can return multiple values in a tuple.
def square_and_cube(number):
    square = number ** 2
    cube = number ** 3
    return square, cube  # Returning both square and cube as a tuple

# Calling the function and unpacking the result
square_result, cube_result = square_and_cube(3)
print(f"The square of 3 is {square_result} and the cube is {cube_result}.")
