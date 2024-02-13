l = [48,56,28,16,73,13,2,9,64,86,93,25,41]
print(l)

print(l.index(28))  #Returns the index of the value
print(l.count(86))  #How many times the value is present in the list

l.append(50)        #It'll add 50 to that list
print(l)
l.sort()            #Sorts list
print(l)
l.sort(reverse=True)    #Sorts list in descending
print(l)
l.reverse()         #Reverses original list
print(l)
l.insert(3,500)     #At 3 put 500
print(l)

#So to make an copy list, we use 
m = l.copy()
# m = l       #m is just a reference, so changes in this will change l
m[0] = 0
print(l)        #Yes it changes, It's not like l remains the same

lst = [65,6548,456,318,156]
l.extend(lst)   #Merges lst into l
print(l)

k = l+m
print(k)        #This creates a new list with l and lst merged