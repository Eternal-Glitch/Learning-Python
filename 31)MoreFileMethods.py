#readline() method, used to read a file line by line

f = open('marks.txt','r')
i = 0
while True:
    i = i+1
    line = f.readline()
    if not line:
        break
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]

    print(f"The marks of student {i} in Math is: {m1}")
    print(f"The marks of student {i} in Science is: {m2}")
    print(f"The marks of student {i} in SS is: {m3}")

#writelines() method, used to write stuff into a file 
    
f = open("myfile1.txt",'w')     #The file is created automatically
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)

#seek() and tell() functions used to work with positions of objects in a file

with open("seek.txt",'r') as f:
    print(type(f))      #Just for info

    f.seek(5)       #It'll seek till 5 

    data = f.read(3)       #This will print 3 stuff after 5
    print(data)

#Tell(), used to show the place we are at currently in a file.
    
    #It will tell where you are, if you've seeked 10, it means that 10 bytes of the file has been skipped and will be read from the next byte....Tell will tell you from where the reading or writing will start

    print(f.tell())

#Truncate()

with open('trunc.txt','w') as f:
    f.write("Hello world!") #First we write in the file
    f.truncate(5)   #We only take 5 bytes of the file and remove the rest, see the file

with open('trunc2.txt','r') as f:
    print(f.read())