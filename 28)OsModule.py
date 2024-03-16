#DO NOT RUN THIS PROGRAM IF YOU ARE NOT AWARE OF WHAT YOU ARE DOING!!!
#Os module contains a lot of functions, it is used to automate all the OS tasks which we perform manually

#You cannot run all the lines together here, should be obvious as you're maipulating files in a multiple ways which is not gonna happen at the same time

import os


if not os.path.exists("ExampleFor28"):
    os.mkdir("ExampleFor28")   #You can use os.path.exists() function with IF, to check if the folder is already made

folder = os.listdir("ExampleFor28")


for i in range(1,101):
    os.mkdir(f"ExampleFor28/Day {i}")  #This was executed first, then renamed it
    os.rename(f"ExampleFor28/Day {i}" , f"ExampleFor28/Tutorial {i}")
    print(os.listdir(f"data/{folder}"))

print(os.getcwd())
os.chdir("/Coding grounds")
print(os.getcwd())


#Os module is a vast world, so go and explore it