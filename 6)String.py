story = """There was once a boy,
had someone to love,
was happy with her and tried to make her happy,
But he got nothing in return and she didn't help him,
He was done baring everything and wanted to leave,
He tried leaving but love brought him back,
But then she left,
Found someone else after some months, and was happy with him,
The boy is still a fool for her,
He might never love anyone the way he did.
"""

# for character in story:
#     print(character)

name = 'Raddish,Gorkan'
print(len(name))
len1 = len(name)
print('A good gamer name should be', len1 , 'characters long.')

#string slicing
animal = "Hippopatamus"
print(len(animal))
print(animal[0:5])  #its like it'll give till 4 not 5.
print(animal[:5])   #python just puts a 0 there, so we can chill out
print(animal[:])   #This one is like the end has the length of the string, it'll print the whole thing [0: the end]
print(animal[5:2])  #Won't print backwards, it doesn't make sense   

#Negative slicing
print(animal[0:-5]) #Here the interpreter puts a formula on the negative thing,[0:len(animal)-5]....so 12-5 = 8 => 0:8
# print(animal[:len(animal)-5])....both are same
print(animal[-6:-3]) #It says len(animal)-6 : len(animal)-3 => 6:9

#String operations/methods (They operate on your string and create new ones)
name = '!!Utkarsh bhai!! !!!'
#strings are immutable so all these strings below are new strings....not converted into upper or lower
print(len(name))
print(name.upper())
print(name.lower())
print(name.rstrip("!"))     #strips trailing characters
print(name.replace("Utkarsh", "Nigg"))
print(name.split(" "))      #I'm spiltting with a space so the string needs to have a space, and this creates a list
print(name.capitalize())    #This captilizes the first letter and rest are lowercased.
print(name.count('Utkarsh'))

pc = 'Welcome to the Console!!!'
print(len(pc))
print(len(pc.center(50)))
print(pc.center(50))

print(name.endswith("!!!")) #Gives a boolean answer, you can use it in if/else
print(name.startswith("!!!")) 
print(pc.endswith("to", 4,10)) #Gives a boolean answer

intro = "He's name is davito, he is a goddamn hacker"
print(intro.find("is"))  #if it ain't there then it returns -1
print(intro.index("is"))  #if it ain't there then it returns an error

alpha = "HiMyNameIsSlim"
print(alpha.isalnum())  #Alpha numeric means that it should have only A-Z,a-z,0-9 =>True/Flase
print(alpha.isalpha())  #Alpha means that it should have only A-Z,a-z =>True/Flase
print(alpha.islower())  #Everything should be lowercase =>True/Flase
print(alpha.isupper())  #Everything should be uppercase =>True/Flase

print(name.isprintable()) #If everything is printable then true, non printable are characters like \n and all that.

space = "     "     #using space
space1 = "      "     #using tab
print(space.isspace())  #isspace checks if the string has white spaces
print(space1.isspace())

print(alpha.istitle())  #True as every word if seperated will be capitalized
print(intro.istitle())  #False as every word is not capitalized

print(intro.swapcase()) #Swaps upper to lowercase and vice-versa

print(intro.title())    #Converts the words in titlecase