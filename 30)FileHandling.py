#Learning how to manipulate a file

#Opening a file

f = open('myfile.txt','r')
#Takes 2 arguments, file and mode
# r => reading (default)     w => writing        a => appending     x => create

f = open('myfile2.txt','w') 
#This will create a file to write, It's not a thing to create a file....but it will if the file doesn't exist
f = open('myfile3.txt','a') 
#This will create a file to append, It's not a thing to create a file....but it will if the file doesn't exist

#We also have to specify how the file should be handled
#T mode is used to handle text file   
f = open('myfile.txt','rt')     #r and rt is same 
f = open('myfile.txt','wt')     #w and wt is same

f = open('myfile.txt','rb')    #b means it'll handle the file as binary

#Reading a file
f = open('myfile.txt','r')
text = f.read()
print(text)
f.close()

#Writing a file
f = open('myfile2.txt','w') 
f.write("Hello world, bow down to my creation!")    #This will overwrite the content inside the file
f.close()       #Without this the write will not execute inside the file 

with open('myfile.txt','a') as f:       #This will close the file automatically
    f.write("Hey i'm inside this thing where close ain't needed")