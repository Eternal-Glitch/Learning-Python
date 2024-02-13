#Two types: 1.Built-in (You don't need to write def)(min(),max(),len(),sum(),etc)  2.User-defined(We write def)

def mid(a,b):       #defining a function with def
    ans = (a+b)/2
    print(ans)

def gmean(a,b):
    ans = (a*b)/(a+b)   #Return (a*b)/(a+b) will also work 
    return ans

def random(a,b):
    pass            #We write pass when we would like to write the function body later, leaving it empty gives error

a = 5
b = 8
mid(a,b)            #Calling a function

c = 10
d = 7
x = gmean(c,d)
print(x)

#Function arguments
# 4 types: 
#1.Default 2.Keyword 3.Variable Length 4.Required

'''Default'''
def avg(a=4, b=6):
    print("Average is", (a+b)/2)
# avg(5)      Here the 5 is value of 'a' and 4 will be overwrite, 'b' will remain same
# avg(b=2)    'b' will be overwrite, 'a' stays same
# avg(5,9)     it'll ignore the one in the function and use the ones here
avg()       

'''Keyword'''
avg(b=8, a=5)     
 #If you write the arguments in any order, that's keyword args

'''Variable Length'''
def tup(*numbers): #*numbers is an iterable, it takes the numbers as a tuple
    sum = 0
    for i in numbers:
        sum = sum + i
    print('Average of the numbers:', sum/len(numbers)) #len will give the number of numbers

tup(2,2,2)

def name(**name):   #This is to take arguments as a dictionary
    print("Hello", name["fname"], name["mname"], name["lname"])

name (fname = 'Utkarsh', mname = 'R', lname = 'Dankhara')


'''Required''' 
avg(3,9)   
#This is used when the function has no defined values => def avg(a,b), in this case you have to pass some value to the function