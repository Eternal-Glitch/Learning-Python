#Well the point of a tuple is that the data cannot be changed or manipulated, so why even learn the methods.
#Changing a tuple will require us to convert it into a list and then back to tuple

countries = ("India", "Japan", "USA", "Russia", "England", "Bolivia", "Africa")

 #That's a tuple inside a list now, well you can't just make a list here with [], it'll take all the items of countries as a single element
temp = list(countries) 

temp.append("Talibaan")
print(temp)
temp.pop(4)
temp[2] = "Spain"
countries = tuple(temp) #Ig it's better to write tuple here too, for less errors in future like the one with the list

print(countries)

#while contactinating two tuples you are creating a new tuple so that's fine

#Well there are some methods for tuples like

num = (10, 12, 18, 15, 10 , 23, 54, 10, 18, 12, 5)
ehh = num.count(10)  #count()
ehh = num.index(4)  #index()
ehh = num.index(10, 3, 8)  #It'll search index of 10 between 3rd and 8th index, searching with slicing basically
ehh = len(num)  #len()
