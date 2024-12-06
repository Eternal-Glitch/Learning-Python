# Class and Object

class detail:
    name = 'Ski'
    age = 19
    def info(self):     # Self is used for the current object on which the function is being called
        print(f"{self.name} is {self.age} years old")


a = detail()
b = detail()

a.name("Poseiden")
a.age(1800)
a.info()    # The data A is carrying will go to self

b.name("Zeus")
b.age(2500)
b.info()    # The data B is carrying will go to self