#When importing, the function will run, either you call it or not

def welcome():
    print("Hey, welcome to my lair....It's the batcave")

print(__name__)

#This basically says that we are running it from here only
if __name__ == "__main__":  #This will make the importing file run the function only once as name won't be equal to main 
    welcome()