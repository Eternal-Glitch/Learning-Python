#Will be used for advanced list manipulation
#It can be used on other objects too, not only lists

#All of these are higher order function, they take a function and an iterable object as an argument
#      MAPS
l = [1,2,5,6,4,8]

cube = lambda x: x*x*x  #You can make a normal function too, but your call

#Give map the name of the function first and then the list you wanna apply the function on each of its elements
newl = list(map(cube, l))   #This will return a map object so we convert it into desired object

print(newl)



#       FILTER

fill = lambda a: a>4        #We made a function
fillList = list(filter(fill, l))  #We make a list to store the result, elements returning true will be stored in the list
print(fillList)

#print(list(filter(fill, l))) => We print the elements by filtering l list with fill function, also we converted it into list



#       REDUCE
#Well first you gotta import reduce

from functools import reduce

num = [1,4,6,3,7,2]
mysum = lambda x,y: x + y

red = reduce(mysum, num)    #Converting this into a list gives and error
# [1,4,6,3,7,2] => 1+4 = 5, according to the function mysum
# [5,6,3,7,2] => 5+6 = 11,
# [11,3,7,2] => 11+3 = 14,
# [14,7,2] => 14+7 = 21,
# [21,2] => 21+2 = 23,
# [23] => the reduce functon will return 23 to red

print(red)
