#fString is used for string formatting
#It makes it easier to store a variable into a string


txt = "My name is {0} and i'm from {1}."    #Indexing will be important if you gonna change the sequence in printing
name = "Utkarsh"
country = "India"

print(txt.format(name, country))            #.format is a method idk for what


#To make all this easier we use fString

print(f"My name is {name} and i'm from {country}.")
print(f"Syntax of f-String: My name is {{name}} and i'm from {{country}}.") #To show this literally we just put curly on it

price = 52.46874564
say = f"The price to buy your freedom is {price: .3f} only!!"   #.3f states to print only till 3 decimals
print(say) 