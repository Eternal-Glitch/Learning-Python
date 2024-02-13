#We use type casting like "25", to add 5 to it....we will use int function to tell python that it's a valid number
#Type casting/Type conversion is to change a datatype into another data type using methods like int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict() etc...

a = "10"
b = "5"
print(a + b)
print(int(a) + int(b))          #type casting(Explicit)

x = 12.8            #float
y = 8               #int
print(x + y)        #python will convert int into float and then add(Implicit type casting)