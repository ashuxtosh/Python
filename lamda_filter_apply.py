
# # lambda
# add = lambda x,y,f: x+y
# print(add(54,x=3,y=4,))

# # filter

# def is_even(n):
#     return n**2 > 10

# print(list(filter(lambda x:x**2 > 10, [1,2,3,4,5,6,7,8,9,10])))

# print(list(filter(is_even, [1,2,3,4,5,6,7,8,9,10])))

# map

# def square(n):
#     return n**2

# print(list(map(square, [1,2,3,4,5,6,7,8,9,10,10])))



from functools import reduce

# # Function to multiply two numbers
def multiply(x, y):
    return x * y

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Use reduce with the multiply function to find the product
product = reduce(multiply, numbers,10,2)

print(product)  # Output: 120


