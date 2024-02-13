#It is an ordered data type since version 3.7
#Dictionary items are key value pairs, separated with commas and inside curly brackets
dict = {'name':'Ski', 'id': 69, 'place':'Gandhinagar'}

#Two ways to fetch the data from the dictionary
print(dict['name'])     #This will give an error
print(dict.get('name')) #This will give none as an ans rather than an error

print(dict.keys())  #This gives all the keys
print(dict.values())  #This gives all the values
print(dict.items())  #This gives all the key-value pairs

for i in dict.keys():
    print(dict[i])

for i,j in dict.items():
    print(f"The key is {i}, with the value {j}")