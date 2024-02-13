# a = input("Enter your name :")
# print("I guess that your name is", a)

x = input("Enter your first number:")
y = input("Enter your second number:")
print("You didn't use type casting or the other method, so")
print(x + y) 
# print(x - y) 
# print(x * y) 
# print(x / y) 
 #This won't work as input function takes the data as a string, so use type casting....OR
print("After using type casting")      
print(int(x) + int(y))

b = int(input("Enter your first number:"))
c = int(input("Enter your second number:"))
print(b + c)
