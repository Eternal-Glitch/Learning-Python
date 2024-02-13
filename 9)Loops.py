#There are two loops....for and while.

name = 'Utkarsh'

for i in name: #Here the name has a string so i is for every character in name, for list it will be every element,etc 
    print(i, end=",")

colors = ["Cyan", "White", "Nigga"]

for color in colors:
    print(color)
    for i in color:
        print(i)

#See in for loop there is no condition nor increament, it just happens
for k in range(10):     #In range it will go till n-1, so here it prints form 0 to 9
    print(k)
for j in range(5,10):   #Here it'll print from 5 to 9
    print(j)
for l in range(0, 10, 2):     #Here the third number is for step, it skips that much between the numbers.
    print(l)


#To make a while loop
i = 0       #we need to first create a variable
while(i<=5):
    print(i)
    i = i+1
else:       #You can use else with while, After the loop stops it'll go into else
    print('Done.')

#There is no do-while loop in pyhton, but the question to make one is surely asked....so here,
#To create a do-while loop
num = 1
while(num > 0):     #Yes we use and infinte loop
    num = int(input("Enter your choice:"))  #You have to keep the number inside the loop or it will start the infinte loop
    print("1. Greetings")
    print("2. Eatings")
    print("3. Fuck OFFs")
    print("4. EXIT")
    if(num == 4):   #You can say this is while condition for a do-while loop
        break

#Another examples for a do-while loop
count = 0
while True:     #False here doesn't allow the code to run, this is just to make an ifinite loop
    print(count)
    count = count + 1
    if(count%100 == 0):     #This is the main condition to get out of the loop
        break

#Another one,
while True:
    count = int(input("Enter number:"))
    print(count)
    if not count>0:     #if-not,it says that when count is not greater than 0
        break

#Important thing:
#You can use else in a for and while loop and let's see how imp that is....
    
for i in range(8):
    print(i)
    if i == 5:
        break       #When this will happen, then the else statement won't execute 

else:           #This will execute when the for loops iterations are executed successfully, it's a part of the loop
    print('i is done giving values.')



#Timepass
for i in range(1,101):
    print("Ram") if i%5 == 0 else print(i) #Yeh it's a shorthand if else