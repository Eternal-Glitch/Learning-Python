a = int(input('Enter your age:'))
print("Your age is:",a)

#Conditional operators
print(a<18)
print(a>18)
print(a<=18)
print(a>=18)
print(a==18)
print(a!=18)
#They gave boolean answers

#if-else
if(a>18):
    print("You can drive so go HAM on them!")
else:
    print("Sorry bro, grow up")

#else if, written as elif
a = int(input('Enter your number:'))
if(a>0):
    print('Your nunber is +ve')
elif(a==0):
    print("The number is 0")
else:
    print('your number is negative.')

#Nested if-else
a = int(input('Enter your number for nested:'))
if(a<0):
    print("Tiny number")
elif(a>0):
    if(a<50 or a>100):
        print('Number is smaller than 50 or greater than 100')
    elif(a>50 and a<100):
        print('Number is between 50 and 100')
    else:
        print('Your number is 50')
else:
    print("Is it even a number?")