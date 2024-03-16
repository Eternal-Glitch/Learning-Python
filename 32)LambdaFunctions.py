#Used to make anonymous functions (Functions with no name, or a function as an expression)

# def avg(x):
#     return x*2

#We can write the same function as a lambda function like this:

double = lambda x: x*2     #A lambda function which takes x as value and returns x*2, being stored in a variable
cube = lambda x: x*x*x  #Returns x^3 
avg = lambda x,y,z:  (x+y+z)/3

#It's better to use these only when you have a one line function, don't compress big functions into this one line.

def trial(fun , value):     #A function having a function as an argument, value will be passed in fun from avg 
    return 7 + fun(value)

print(double(5))
print(cube(5))
print(avg(5,3,10))

print(trial(avg,2))     
#You can also write => lambda x,y,z:  (x+y+z)/3 => in place of avg if you feel like not making a variable 