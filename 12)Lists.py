#Lists are used to store different data into 1 thing

l = [4,6,9, 'Ski', True, "Witless", 1, False]     #This is a list
print(l)

#Positive index
print(l[0])
print(l[1])
print(l[2])

#Negative index
print(l[-3])    #Same like string, len(l)-3 =>2 
# print(l[len(l)-3])
# print(l[5-3])
# print(l[2])
print(l[-5])

if "Ski" in l:
    print("Got it!")
else:
    print("Sorry Master.")
#All this applies for strings as well
if "i" in "Ski":
    print("Yehh")
else:
    print("Nope")

print(l[:])         #Same as print(l)
print(l[1:-4])      #Slicing
print(l[0:6:2])     #Jump index, here it'll jump 2 spaces and print the element in the list


#List comprehension
lst = [i for i in range(10)]        #i*i will give result as => 0,1,4,9,16,25...till 100
print(lst)

lst = [i for i in range(10) if i%2 == 0]        #We can also put a condition
print(lst)