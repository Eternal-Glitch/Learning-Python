x = int(input('Enter the value for x:'))

#This is just like switch case from C, C++
match x:
    case 1:
        print('Your number is 1')   #We don't use break here, as if the condition is matched then it breaks 
    case 2:
        print('Your number is 2')
    case 3:
        print('Your number is 3')
    case 4:
        print('Your number is 4')
    case 5:
        print('Your number is 5')
    case _ if x <10:                #This is how we use default statement with a condition
        print('Your number is greater than 10')
    case _ if x >10:
        print('Your number is between 5 and 10')
    case _:                         #This is the final default statement
        print('Your number is negative')

y = str(input("Enter your favourite Letter:"))

# match y:
#     case A,Z:
#         print("Your letter seems capital")
#     case a,z:
#         print('Your letter seems')