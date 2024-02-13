#We are going to make a program to encrypt a code by following a set of rules as per the user and then decrypt it.
#Strings are immutable, so find something else

msg = input("Enter your secret message:")
lst = (msg.split(" "))

#Rules to encrypt:
#1.Reverse front half the word and add 3 random character in the end
#2.Reverse it normally if the word is atmost 3 letters
for i in range(len(lst)):
    if(len(lst[i])<4):
        lst[i] = lst[i][::-1]
        print(lst[i])
    else:
        mid = len(lst[i])/2
        lst[i] = half[::-1]
        print(lst[i])


#Rules to decrypt:
#1.Reverse front half of the word and remove 3 random character in the end
#2.Reverse it normally if the word is atmost 3 letters



# Tyranosauras => a, a(0) = T, mid = 12/2 = 6,