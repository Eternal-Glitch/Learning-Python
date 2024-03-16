#Try not to use this as it may cause confusion in understanding the code, as you'd be changing a global inside a function and then using the changed value outside the function

x = 10  #Global variable

def fun():
    global x    #This will make the variable x global making it temperable inside a function
    x = 6       #This should be a local variable, but it's global
    y = 3       #Local variable
    print(y)

fun()
print(x)
#print(y)        #It'll throw an error as y is a local variable which you are trying to use outside it's area