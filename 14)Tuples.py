#A tuple cannot be changed 
#The only difference between lists and tuples are that tuples cannot be changed....Nor the data nor the length
#Strings and Tuples are immutable, lists are mutable

tup = ()    #tup is just the name, the brackets shows it's a tuple
tup = (1)   #This will give type int, so to make a tuple do this tup = (1,)   

print(type(tup), tup)

tuple = (1, 47, 84, 23, 99, "Blue", True) 
# tup[0] = 55     #This will give an error as tuples cannot be changed....the data will be permanent
print(tuple[0])
print(tuple[1])
print(tuple[-2])    #Negative indexing

#A lot of things in list will be present here

if 83 in tuple:
    print("Found it!")
else:
    print('Nope')

tup2 = tuple[1:4]   #Slicing
print(tup2)