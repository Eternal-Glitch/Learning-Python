#You can use it when you have to write a small if statement
#It will make the readability worse for complex if else statements so use it for short stuff

a = 50
b = 250
print("A") if a>b else print("=") if a == b else print("B") #Pretty read-able thing

c = 9 if a>b else ''     #Putting a double/single quote and writing else here is imp, or it'll give error
print(c)

#A syntax if you can inderstand:    value_if_true "if" condition "else" value_if_false