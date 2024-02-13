#We kinda know it, it's when you call a function inside a function

#Factorial
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)    #Ex:5, 5*4*3*2*1 => 5 * fact(4)

print(fact(3)) 
print(fact(4)) 
print(fact(5)) 
print(fact(6)) 

# 4 * fact(3)
# 4 * 3 * fact(2)
# 4 * 3 * 2 * fact(1)
# 4 * 3 * 2 * 1