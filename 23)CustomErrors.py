#We will use raise keywords for this

a = int(input("Enter a number between 4 and 8")) #Remember, input will take the data as string, so convert with type casting

if a<4 or a>8:
    raise ValueError("Out of bounds!")

# if int(a) == True:
#     print("You might be right")
# elif a=='quit':
#     print("QUIT")

# if type(a)==str:
#     if a=='quit':
#         print('Okay, see ya')
#     else:
#         raise NameError("Wrong input to quit I see")

#Making a program where writing any string will give an error except 'quit'
b = input("Enter what you like:")

if b == 'quit':
    print('You have exited the program.')
else:
    try:
        if int(b)>0:    
            print('It is a number')
    except:
        raise ValueError("What did you even write there??")

#Raising an error in the except also displays the error occured in try too, if you only print a statement in except then it won't show the try error and display except(weird it seems)


#You can define custom errors by creating a class which should be derived from exception class(A built in class)