marks = [14, 64, 75, 99, 14, 1, 10]

'''
index = 0
for mark in marks:
    print(mark)
    if(index == 3):
        print("Me is awesome.")
    index += 1'''      #You cannot write =+, it won't give error but won't give the solution too

#To make this a litlle better we can use enumerate functions

#This function gives the index and the value at the same time
for index, mark in enumerate(marks, start = 1):    #The start is to tell py where to start from, not writing it is fine
    #The enumerate function will give the index one by one with the values of the list
    print(mark)
    if(index == 3):
        print("Me is awesome.")

#By writing 2 values in the for loop, index will get the first value of tuple and mark will get second value of tuple.
        #Yeh enumerate creates a tuple