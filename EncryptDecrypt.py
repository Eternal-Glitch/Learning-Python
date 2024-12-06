#We are going to make a program to encrypt a code by following a set of rules as per the user and then decrypt it.
#Strings are immutable, so find something else

import random

#Rules to encrypt:
#1.Reverse front half the word and add 3 random character in the end
#2.Reverse it normally if the word is atmost 3 letters

def encrypt():
    msg = input("Enter your secret message:")
    lst = (msg.split(" "))
    for i in range(len(lst)):

        if(len(lst[i])<4):      #Words with 3 letter or less need normal reversing
            word = lst[i]
            lst[i] = word[::-1]
            
        else:                   #Reversing of the longer words
            mid = len(lst[i])/2
            word = lst[i]
            f1 = random.choice(word) + random.choice(word) + random.choice(word)
            half = word[:int(mid)]
            secondHalf = word[int(mid):]
            lst[i] =  half[::-1] + secondHalf + f1   #front reversed + back same + Random letter
            
    code = " ".join(lst)        #Join function works with the value at the start
    print(code)

#Rules to decrypt:
#1.Reverse front half of the word and remove 3 random character in the end
#2.Reverse it normally if the word is atmost 3 letters

def decrypt():
    msg = input("Enter your secret message:")
    lst = (msg.split(" "))
    for i in range(len(lst)):

        if(len(lst[i])<4):      #Words with 3 letter or less needs normal reversing
            word = lst[i]
            lst[i] = word[::-1]
            

        else:                   #Solving of the longer words
            word = lst[i]
            word = word[:-3]
            mid = len(word)/2
            half = word[:int(mid)]
            secondHalf = word[int(mid):]
            lst[i] = half[::-1] + secondHalf   
            
    print(" ".join(lst))        #Join function works with the value at the start


while(True):
    print("1. Encrypt a message.")
    print("2. Decrypt a message.")
    print("3. EXIT.")
    n = int(input("Enter your choice: "))
    match n:
        case 1:
            encrypt()
        case 2:
            decrypt()
        case 3:
            break 
        case _:
            print("INVALID INPUT")

    if(n==3):
        break