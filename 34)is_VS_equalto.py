# BOTH ARE COMPARISON OPERATORS
# The is keyword comparse the location in the memory
# == compares the values

a = [1,2,3]
b = [1,2,3]
print(a is b)   # False
print(a == b)   # True

# Here python will not take up another memory location for the second 3, instead it will make A and B both point at 3
# Same for strings and tuples
a = 3
b = 3
print(a is b)   # True
print(a == b)   # True
