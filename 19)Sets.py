#Mainly used to reduce redundancy
#It's an unordered collection of data, you cannot change sets
s1 = {2,8,6,2,4,8}
print(s1)
#A lot of methods which are used in list can be used here

info = {"Supp", 20, 5.21, True, 20}
print(info)

new = {}    #This is not an empty set, it's a dictionary
new1 = set()    #This is an empty set


for i in info:
    print(i)

#Methods for sets
s2 = {5,8,7}
print(s1.union(s2)) #s1 and s2 are not changed here, it just shows a union set
s1.update(s2)   #s1 is being updated here to => s1 U s2

print(s1.intersection(s2))
s1.intersection_update(s2)  #s1 is being updated here to => s1 n s2

print(s1.symmetric_difference(s2))  #This will give the elements which are not common

print(s1.difference(s2))    #Kinda a-b, gives things of s1 which are not in s2

print(s1.isdisjoint(s2))    #Checks if both the sets have different elements

print(s1.issuperset(s2))    #Checks if s2 is subset of s1, or does s2 elements belong to s1

print(s1.issubset(s2))      #Checks if s1 is subset of s2

s1.add(10)  #Adds items

s1.remove(8)    #This will throw and error if the item is not there
s1.discard(20)   #This won't throw and error

gone = s1.pop()    #Will pop a random element out of the set, to see it, store it into something and print that

del s1  #Deletes the set
s2.clear()  #Clears the data in the set, the set won't be deleted