#Well we will learn how to handle an error and continue our code

a = input("Enter your number:")

try:    #If this executes then well and good
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except: #This will execute during an error and then break to continue ahead, (except exception as e, gotta see what this is)
    print("Some error occurred")

#We can use multiple except keywords and use them with methods like, ValueError, IndexError etc.

print("Some imp code")
print("The end of the program")

#We can use Finally clause in exception handling to do clean-ups
#The code inside this will always execute no matter if there is error or not

try:
    l = [1,5,4,8]
    i = int(input("Enter index to see:"))
    print(l[i])
except:
    print('Error occurred, sorry to bother.')
finally:
    print("I will always execute no matter what.")
'''
So you might think why even use finally when you can use a normal statement outside the try-except

Well when this thing is in a function then you might wanna return a value and finally won't execute, so to return a value as well as execute the finally statement we use this.

Finally means it will execute even though you want a value returned from the function, normally after returning it should just break but finally will execute no matter what'''