# It is used to define some variables as default when creating an object

class details:
    def __init__(self,n,a):     # This __init__ is used as a constuctor
        self.name = n   # n is required argument, if not provided a value, it will give error
        self.age = a    # a is a default argument, intialized to 0
    def info(self):
        print(f"{self.name} is {self.age} years old")

a = details("Ski",19)   # When this executes, the constructor will run automatically
b = details("Zeus", 20000)
a.info()
b.info()

# A and B are passed automatically to self, it's a rule so....follow it

# Types of constructors:
    # 1. Default constructor - __init__(self)
    # 2. Parameterized constructor - __init__(self, a, b)

    # You can know about these later:
    # 3. Copy constructor - __init__(self, obj)
    # 4. Static constructor - __init__(cls)
    # 5. Private constructor - __init__(self, a, b) - private constructor is not accessible outside the class
    # 6. Final constructor - __init__(self, a, b) - final constructor is not accessible outside the class